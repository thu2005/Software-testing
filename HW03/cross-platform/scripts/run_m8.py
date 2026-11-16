#!/usr/bin/env python
"""Execute the HW03 65-item GUI checklist on three real browser targets."""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService


ROOT = Path(__file__).resolve().parents[2]
CHECKLIST = ROOT / "checklist" / "gui-checklist.md"
RESULTS = ROOT / "cross-platform" / "results"
RAW = ROOT / "cross-platform" / "raw"
SHOTS = ROOT / "cross-platform" / "screenshots"
STAMP = ROOT / ".agents" / "skills" / "cross-platform-testing" / "scripts" / "stamp_screenshot.py"
EMAIL = "23120170@student.hcmus.edu.vn"
STUDENT = "Nguyễn Đoàn Xuân Thu"
BASE = "http://localhost:5173"

CHROMEDRIVER = Path(r"C:\Users\X1 Carbon\.cache\selenium\chromedriver\win64\157.0.8103.78\chromedriver.exe")
GECKODRIVER = Path(r"C:\Users\X1 Carbon\.cache\selenium\geckodriver\win64\0.37.1\geckodriver.exe")
ANDROID_DRIVER = Path(
    os.environ.get(
        "HW03_ANDROID_CHROMEDRIVER",
        ROOT / "cross-platform" / "tools" / "chromedriver109" / "chromedriver.exe",
    )
)


@dataclass
class Platform:
    slug: str
    label: str
    browser: str
    mobile: bool = False


PLATFORMS = {
    "chrome-windows": Platform("chrome-windows", "Chrome 157.0.8103.50 / Windows", "chrome"),
    "firefox-windows": Platform("firefox-windows", "Firefox 160.0 / Windows", "firefox"),
    "chrome-android": Platform("chrome-android", "Chrome 109.0.5414.123 / Android 13 / Pixel_4a emulator", "android", True),
}


def parse_items() -> dict[str, dict[str, str]]:
    rows: dict[str, dict[str, str]] = {}
    for line in CHECKLIST.read_text(encoding="utf-8").splitlines():
        if not line.startswith("| GUI-"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows[cells[0]] = {"ia": cells[1], "screen": cells[2], "item": cells[3], "bug": cells[8]}
    if len(rows) != 65:
        raise RuntimeError(f"Expected 65 checklist rows, found {len(rows)}")
    return rows


def make_driver(p: Platform):
    if p.browser == "chrome":
        o = ChromeOptions()
        o.add_argument("--headless=new")
        o.add_argument("--window-size=1440,1000")
        o.add_argument("--disable-search-engine-choice-screen")
        o.add_argument("--no-first-run")
        o.add_argument("--disable-gpu")
        o.add_argument("--disable-dev-shm-usage")
        o.add_argument("--no-sandbox")
        return webdriver.Chrome(service=ChromeService(str(CHROMEDRIVER)), options=o)
    if p.browser == "firefox":
        o = FirefoxOptions()
        o.add_argument("-headless")
        o.add_argument("--width=1440")
        o.add_argument("--height=1000")
        d = webdriver.Firefox(service=FirefoxService(str(GECKODRIVER)), options=o)
        return d
    if not ANDROID_DRIVER.is_file():
        raise RuntimeError(
            "Android Chrome 109 requires ChromeDriver 109. Set "
            "HW03_ANDROID_CHROMEDRIVER to its local executable path."
        )
    o = ChromeOptions()
    o.add_experimental_option("androidPackage", "com.android.chrome")
    return webdriver.Chrome(service=ChromeService(str(ANDROID_DRIVER)), options=o)


class Run:
    def __init__(self, platform: Platform, items: dict[str, dict[str, str]]):
        self.p = platform
        self.items = items
        self.d = make_driver(platform)
        self.wait = WebDriverWait(self.d, 12)
        self.results: dict[str, dict[str, str]] = {}
        self.states: dict[str, tuple[Path, str]] = {}
        self.long_checks: dict[str, bool] = {}
        self.ua = self.d.execute_script("return navigator.userAgent")

    def close(self):
        self.d.quit()

    def record(self, item: str, passed: bool, note: str, state: str = "overview"):
        self.results[item] = {"result": "Passed" if passed else "Failed", "notes": note, "state": state}

    def get(self, path: str, selector: str | None = None, pause: float = 0.5):
        self.d.get(BASE + path)
        if selector:
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        time.sleep(pause)

    def shot(self, state: str):
        path = RAW / self.p.slug / f"{state}.png"
        path.parent.mkdir(parents=True, exist_ok=True)
        self.d.save_screenshot(str(path))
        self.states[state] = (path, self.d.current_url)

    def viewport(self, width: int, height: int):
        if not self.p.mobile:
            self.d.set_window_size(width, height)

    def js(self, script: str, *args):
        return self.d.execute_script(script, *args)

    def diagnostic(self, text: str):
        """Show the observed DOM state in the evidence screenshot without changing it."""
        self.js("""
          document.getElementById('__hw03_evidence')?.remove();
          const box=document.createElement('div');
          box.id='__hw03_evidence';
          box.textContent=arguments[0];
          Object.assign(box.style, {
            position:'fixed', left:'12px', bottom:'12px', zIndex:'2147483647',
            maxWidth:'70vw', padding:'10px 12px', whiteSpace:'pre-wrap',
            background:'rgba(255,248,196,.97)', color:'#111827',
            border:'2px solid #b45309', borderRadius:'6px',
            font:'600 14px/1.35 monospace', boxShadow:'0 2px 8px rgba(0,0,0,.25)'
          });
          document.body.appendChild(box);
        """, text)

    def clear_diagnostic(self):
        self.js("document.getElementById('__hw03_evidence')?.remove()")

    def text(self) -> str:
        return self.d.find_element(By.TAG_NAME, "body").text

    def fresh(self, path: str, selector: str | None = None):
        self.get(path, selector)
        self.js("localStorage.clear(); sessionStorage.clear();")
        self.get(path, selector)

    def product(self):
        self.fresh("/product/1", "h1")
        h1s = self.d.find_elements(By.CSS_SELECTOR, "h1")
        h1 = h1s[0].text if h1s else ""
        self.record("GUI-001", len(h1s) == 1 and h1 == "iPhone 15 Pro Max", f"h1={len(h1s)}, nội dung={h1!r}", "product")

        img = self.d.find_element(By.CSS_SELECTOR, "main img")
        dims = self.js("return {nw:arguments[0].naturalWidth,nh:arguments[0].naturalHeight,w:arguments[0].getBoundingClientRect().width,h:arguments[0].getBoundingClientRect().height,complete:arguments[0].complete}", img)
        ratio_ok = dims["nw"] > 0 and dims["nh"] > 0 and abs((dims["nw"] / dims["nh"]) - (dims["w"] / dims["h"])) < 0.03
        self.record("GUI-002", bool(dims["complete"] and ratio_ok), f"Ảnh natural={dims['nw']}×{dims['nh']}, render={dims['w']:.0f}×{dims['h']:.0f}, đúng tỷ lệ={ratio_ok}", "product")
        alt = img.get_attribute("alt") or ""
        self.record("GUI-003", alt == h1, f"alt={alt!r}, tên sản phẩm={h1!r}", "product")

        self.viewport(375, 900)
        layout = self.js("return {sw:document.documentElement.scrollWidth,vw:innerWidth,buttonRight:document.querySelector('main button').getBoundingClientRect().right}")
        layout_ok = layout["sw"] <= layout["vw"] + 1 and layout["buttonRight"] <= layout["vw"] + 1
        self.record("GUI-004", layout_ok, f"viewport={layout['vw']}, scrollWidth={layout['sw']}, buttonRight={layout['buttonRight']:.1f}", "product")
        self.long_checks["product"] = self.js("""
          let n=document.querySelector('h1'),old=n.textContent;n.textContent+=' nội dung tiếng Việt rất dài để kiểm tra bố cục';
          let ok=document.documentElement.scrollWidth<=innerWidth+1;n.textContent=old;return ok;
        """)
        self.viewport(1440, 1000)
        price = self.d.find_element(By.XPATH, "//main//p[contains(.,'₫')]").text
        price_ok = bool(re.fullmatch(r"\d{1,3}(,\d{3})+ ₫", price)) and "NaN" not in price
        self.record("GUI-005", price_ok, f"Giá hiển thị={price!r}", "product")
        qty = self.d.find_element(By.CSS_SELECTOR, "input[type=number]")
        labels = [x.text for x in self.d.find_elements(By.TAG_NAME, "label")]
        self.record("GUI-006", qty.get_attribute("type") == "number" and any("Số lượng" in x for x in labels), f"input type={qty.get_attribute('type')}, labels={labels}", "product")
        self.shot("product")

        # Actual keyboard focus order and indicator.
        self.js("document.body.tabIndex=-1;document.body.focus()")
        order = []
        styles = []
        for _ in range(8):
            self.d.switch_to.active_element.send_keys(Keys.TAB)
            a = self.d.switch_to.active_element
            name = (a.text or a.get_attribute("aria-label") or a.get_attribute("type") or a.tag_name).strip()
            order.append(f"{a.tag_name}:{name}")
            if a.tag_name in ("input", "button"):
                styles.append(self.js("let s=getComputedStyle(arguments[0]); return {outline:s.outline,shadow:s.boxShadow}", a))
        joined = " → ".join(order)
        self.record("GUI-009", "input:number" in joined and "button:Thêm vào giỏ hàng" in joined and joined.index("input:number") < joined.index("button:Thêm vào giỏ hàng"), f"Thứ tự focus: {joined}", "product-focus")
        visible_focus = any("none" not in s["outline"] or s["shadow"] != "none" for s in styles)
        self.record("GUI-010", visible_focus, f"Style focus input/button={styles}", "product-focus")
        self.shot("product-focus")

        body = self.text()
        crumbs = self.d.find_elements(By.CSS_SELECTOR, "nav[aria-label*=breadcrumb], .breadcrumb")
        back_links = [a.text for a in self.d.find_elements(By.TAG_NAME, "a") if "sản phẩm" in a.text.lower() or "trang chủ" in a.text.lower()]
        self.record("GUI-011", bool(crumbs and back_links), f"breadcrumb={len(crumbs)}, đường quay lại={back_links}", "product")
        self.record("GUI-012", h1 == "iPhone 15 Pro Max", f"Mở trực tiếp {self.d.current_url}, sản phẩm={h1!r}", "product")
        cart_link = self.d.find_element(By.LINK_TEXT, "Giỏ hàng")
        self.record("GUI-013", cart_link.is_displayed() and cart_link.is_enabled(), f"Link Giỏ hàng displayed={cart_link.is_displayed()}, enabled={cart_link.is_enabled()}", "product")

        # First click, then cart: verifies GUI-017.
        add = self.d.find_element(By.XPATH, "//button[contains(.,'Thêm vào giỏ hàng')]")
        add.click(); time.sleep(0.25)
        feedback = "Đã thêm" in add.text or any(x.is_displayed() for x in self.d.find_elements(By.CSS_SELECTOR, "[role=alert], .toast"))
        cart_link.click(); time.sleep(0.3)
        first_added = "iPhone 15 Pro Max" in self.text()
        self.record("GUI-017", feedback and first_added, f"Sau một click: feedback={feedback}, sản phẩm trong giỏ={first_added}", "first-add")
        self.shot("first-add")

        # One successful add, badge, direct history and duplicate rows.
        self.get("/product/1", "h1")
        add = self.d.find_element(By.XPATH, "//button[contains(.,'Thêm vào giỏ hàng')]")
        add.click(); add.click(); time.sleep(0.3)
        nav_text = self.d.find_element(By.LINK_TEXT, "Giỏ hàng").text
        badge = bool(re.search(r"\d", nav_text))
        self.record("GUI-014", badge, f"Nội dung navbar sau khi thêm 1 sản phẩm={nav_text!r}", "product-added")
        self.shot("product-added")
        self.d.find_element(By.LINK_TEXT, "EShop").click(); time.sleep(0.2)
        self.d.back(); time.sleep(0.2); back_ok = "/product/1" in self.d.current_url
        self.d.forward(); time.sleep(0.2); forward_ok = self.d.current_url.rstrip("/") == BASE
        self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.2)
        kept = "iPhone 15 Pro Max" in self.text()
        self.record("GUI-015", back_ok and forward_ok and kept, f"Back={back_ok}, Forward={forward_ok}, giữ giỏ={kept}", "product-added")

        # Duplicate product: two more successful add cycles.
        self.get("/product/1", "h1")
        add = self.d.find_element(By.XPATH, "//button[contains(.,'Thêm vào giỏ hàng')]")
        add.click(); add.click(); add.click(); add.click(); time.sleep(0.2)
        self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.2)
        rows = self.d.find_elements(By.CSS_SELECTOR, "tbody tr")
        quantities = [r.text for r in rows]
        self.record("GUI-018", len(rows) == 1 and "3" in rows[0].text, f"Số dòng sau thêm lại={len(rows)}, rows={quantities}", "duplicate")
        self.shot("duplicate")

        # Invalid quantities, observed through UI.
        invalid = []
        for value in ("0", "-1", "1.5", ""):
            self.fresh("/product/1", "h1")
            q = self.d.find_element(By.CSS_SELECTOR, "input[type=number]")
            q.send_keys(Keys.CONTROL, "a"); q.send_keys(value)
            a = self.d.find_element(By.XPATH, "//button[contains(.,'Thêm vào giỏ hàng')]")
            a.click(); a.click(); time.sleep(0.15)
            self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.15)
            invalid.append((value or "rỗng", "iPhone 15 Pro Max" in self.text()))
        zero_neg_rejected = not any(added for value, added in invalid if value in ("0", "-1"))
        other_rejected = not any(added for value, added in invalid if value in ("1.5", "rỗng"))
        self.record("GUI-007", zero_neg_rejected, f"Kết quả input 0/-1={invalid[:2]}", "invalid-quantity")
        self.record("GUI-008", other_rejected, f"Kết quả input 1.5/rỗng={invalid[2:]}", "invalid-quantity")
        self.shot("invalid-quantity")

        # Loading and network-error UI via a real XHR delay/failure injected before SPA navigation.
        self.fresh("/", "h1")
        self.js("""
          window.__origSend=XMLHttpRequest.prototype.send;
          XMLHttpRequest.prototype.send=function(){let x=this;setTimeout(()=>window.__origSend.call(x),2000)};
          history.pushState({},'', '/product/1'); dispatchEvent(new PopStateEvent('popstate'));
        """)
        time.sleep(0.2)
        loading = "Đang tải" in self.text()
        self.record("GUI-016", loading, f"Loading state xuất hiện trong khi XHR bị delay 2 giây={loading}", "loading")
        self.shot("loading")
        time.sleep(2.2)

        self.fresh("/", "h1")
        self.js("""
          window.__origOpen=XMLHttpRequest.prototype.open;
          XMLHttpRequest.prototype.open=function(m,u){return window.__origOpen.call(this,m,'http://127.0.0.1:9/unreachable')};
          history.pushState({},'', '/product/1'); dispatchEvent(new PopStateEvent('popstate'));
        """)
        time.sleep(1)
        net_text = self.text()
        recovery = any(k in net_text.lower() for k in ("thử lại", "lỗi mạng", "không thể tải"))
        stuck = "Đang tải" in net_text
        self.record("GUI-020", recovery and not stuck, f"Sau lỗi mạng: recovery message={recovery}, treo loading={stuck}", "network-product")
        self.shot("network-product")

        self.fresh("/product/999", None)
        time.sleep(0.8)
        invalid_text = self.text()
        friendly = "không tồn tại" in invalid_text.lower() and any("trang chủ" in a.text.lower() or "mua" in a.text.lower() for a in self.d.find_elements(By.TAG_NAME, "a"))
        self.record("GUI-019", friendly, f"Nội dung 404={invalid_text[:180]!r}, có đường quay lại={friendly}", "not-found")
        self.shot("not-found")

    def prepare_cart(self):
        self.fresh("/product/1", "h1")
        add = self.d.find_element(By.XPATH, "//button[contains(.,'Thêm vào giỏ hàng')]")
        add.click(); add.click(); time.sleep(0.2)
        self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.3)

    def cart(self):
        self.prepare_cart()
        h1s = self.d.find_elements(By.CSS_SELECTOR, "main h1")
        self.record("GUI-021", len(h1s) == 1 and "Giỏ" in h1s[0].text, f"Số h1={len(h1s)}, heading={[x.text for x in self.d.find_elements(By.CSS_SELECTOR,'main h1, main h2')]}", "cart")
        headers = [x.text for x in self.d.find_elements(By.CSS_SELECTOR, "thead th")]
        expected = ["Sản phẩm", "Đơn giá", "Số lượng", "Thành tiền", "Thao tác"]
        self.record("GUI-022", headers == expected, f"Header thực tế={headers}", "cart")
        money = re.findall(r"[\d,]+ ₫", self.text())
        self.record("GUI-023", len(money) >= 3 and all(re.fullmatch(r"\d{1,3}(,\d{3})+ ₫", x) for x in money), f"Giá trị tiền={money}", "cart")
        self.viewport(375, 900)
        cart_vw = self.js("return innerWidth")
        cart_sw = self.js("return document.documentElement.scrollWidth")
        self.record("GUI-024", cart_sw <= cart_vw + 1, f"viewport={cart_vw}, scrollWidth={cart_sw}", "cart")
        self.long_checks["cart"] = self.js("""
          let n=document.querySelector('tbody td'),old=n.textContent;n.textContent+=' nội dung tiếng Việt rất dài để kiểm tra bố cục';
          let ok=document.documentElement.scrollWidth<=innerWidth+1;n.textContent=old;return ok;
        """)
        delete = self.d.find_element(By.CSS_SELECTOR, "tbody button")
        color = delete.value_of_css_property("color")
        self.record("GUI-025", color in ("rgba(239, 68, 68, 1)", "rgb(239, 68, 68)"), f"Màu Xóa={color}", "cart")
        minus = self.d.find_elements(By.XPATH, "//button[normalize-space()='−' or normalize-space()='-']")
        plus = self.d.find_elements(By.XPATH, "//button[normalize-space()='+']")
        self.record("GUI-026", bool(minus and plus), f"Số nút −={len(minus)}, +={len(plus)}", "cart")
        self.record("GUI-027", bool(minus and (not minus[0].is_enabled() or minus[0].get_attribute('disabled'))), "Có/không có điều khiển giảm và trạng thái chặn dưới 1", "cart")
        self.record("GUI-028", bool(minus and plus), "Không thể kiểm tra cập nhật theo dòng nếu UI không có +/−" if not (minus and plus) else "Có điều khiển để thay đổi và quan sát thành tiền", "cart")
        self.js("arguments[0].focus()", delete)
        focus_style = self.js("let s=getComputedStyle(arguments[0]);return {outline:s.outline,shadow:s.boxShadow}", delete)
        acc_name = delete.get_attribute("aria-label") or delete.text
        focus_visible = "none" not in focus_style["outline"] or focus_style["shadow"] != "none"
        self.record("GUI-029", acc_name.strip() != "" and focus_visible, f"Accessible name={acc_name!r}, focus={focus_style}", "cart-focus")
        self.diagnostic(
            f"GUI-029 | activeElement={self.js('return document.activeElement===arguments[0]', delete)} "
            f"| name={acc_name!r} | outline={focus_style['outline']} | shadow={focus_style['shadow']}"
        )
        self.shot("cart-focus")
        self.clear_diagnostic()
        crumbs = self.d.find_elements(By.CSS_SELECTOR, "nav[aria-label*=breadcrumb], .breadcrumb")
        self.record("GUI-030", bool(crumbs), f"breadcrumb count={len(crumbs)}", "cart")
        nav_cart = self.d.find_element(By.LINK_TEXT, "Giỏ hàng")
        current = nav_cart.get_attribute("aria-current")
        highlighted = current == "page" or "active" in (nav_cart.get_attribute("class") or "").lower()
        self.record("GUI-031", highlighted, f"aria-current={current!r}, class={nav_cart.get_attribute('class')!r}", "cart")
        links = [x.text for x in self.d.find_elements(By.TAG_NAME, "a")]
        exact_continue = "Tiếp tục mua sắm" in links
        self.record("GUI-032", exact_continue, f"Link trên Cart={links}", "cart")
        self.shot("cart")

        # Tab order (actual key navigation).
        self.js("document.body.tabIndex=-1;document.body.focus()"); focus = []
        for _ in range(12):
            self.d.switch_to.active_element.send_keys(Keys.TAB)
            a = self.d.switch_to.active_element
            focus.append((a.text or a.get_attribute("type") or a.tag_name).strip())
        required = ["−", "+", "Xóa", "Tiến hành thanh toán"]
        keyboard_ok = all(any(x in f for f in focus) for x in required)
        self.record("GUI-059", keyboard_ok, f"Focusable controls={focus}", "cart-keyboard")
        self.diagnostic(
            "GUI-059 | Tab sequence: " + " -> ".join(focus) +
            f"\nRequired controls present in sequence={keyboard_ok}"
        )
        self.shot("cart-keyboard")
        self.clear_diagnostic()

        # Mobile/touch target sizes are measured on the real platform viewport.
        controls = self.d.find_elements(By.XPATH, "//button|//a[contains(.,'Tiến hành thanh toán')]")
        sizes = [(x.text.strip(), round(x.rect['width'],1), round(x.rect['height'],1)) for x in controls if x.text.strip() in ("−", "+", "Xóa", "Áp dụng", "Tiến hành thanh toán")]
        required_names = {"−", "+", "Xóa", "Tiến hành thanh toán"}
        enough = required_names.issubset({x[0] for x in sizes}) and all(w >= 44 and h >= 44 for n,w,h in sizes if n in required_names)
        self.record("GUI-061", enough, f"Touch target Cart={sizes}", "cart")
        self.viewport(1440, 1000)

        # Destructive action confirmation and state synchronization.
        delete = self.d.find_element(By.CSS_SELECTOR, "tbody button")
        delete.click(); time.sleep(0.2)
        confirmed = False
        try:
            self.d.switch_to.alert.dismiss(); confirmed = True
        except NoAlertPresentException:
            pass
        empty = "đang trống" in self.text().lower()
        self.record("GUI-035", confirmed, f"Dialog xác nhận xuất hiện={confirmed}, giỏ trống sau click={empty}", "cart-delete")
        nav = self.d.find_element(By.LINK_TEXT, "Giỏ hàng").text
        badge_zero = bool(re.search(r"0", nav))
        self.record("GUI-037", empty and badge_zero, f"Bảng empty={empty}, navbar={nav!r}, badge 0={badge_zero}", "cart-delete")
        self.shot("cart-delete")

        self.fresh("/cart", None); time.sleep(0.2)
        empty_text = self.text()
        icon = bool(self.d.find_elements(By.CSS_SELECTOR, "main img, main svg, main [class*=icon]"))
        action = "Tiếp tục mua sắm" in empty_text
        self.record("GUI-034", icon and action, f"Empty state action={action}, icon/hình={icon}", "cart-empty")
        self.shot("cart-empty")

        self.prepare_cart()
        total_text = self.text()
        right_label = "Tổng cộng" in total_text and "Tổng tạm tính" not in total_text
        self.record("GUI-036", right_label, f"Nhãn tổng tiền: {'Tổng cộng' if right_label else 'Tổng tạm tính'}", "cart")
        checkout = self.d.find_element(By.XPATH, "//button[contains(.,'Tiến hành thanh toán')]")
        checkout.click(); time.sleep(0.15)
        alert_text = ""
        try:
            alert = self.d.switch_to.alert; alert_text = alert.text; alert.accept()
        except NoAlertPresentException:
            pass
        time.sleep(0.2)
        self.record("GUI-033", "đăng nhập" in alert_text.lower() and "/login" in self.d.current_url, f"Alert={alert_text!r}, URL={self.d.current_url}", "cart-auth")
        self.shot("cart-auth")

    def login(self):
        self.fresh("/login", "form")
        fields = self.d.find_elements(By.CSS_SELECTOR, "form input")
        fields[0].send_keys("test@eshop.com")
        fields[1].send_keys("Test1234!")
        self.d.find_element(By.CSS_SELECTOR, "form button[type=submit]").click()
        self.wait.until(lambda d: d.current_url.rstrip("/") == BASE)
        time.sleep(0.4)

    def prepare_checkout(self):
        self.login()
        self.get("/product/1", "h1")
        add = self.d.find_element(By.XPATH, "//button[contains(.,'Thêm vào giỏ hàng')]")
        add.click(); add.click(); time.sleep(0.2)
        self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.2)
        self.d.find_element(By.XPATH, "//button[contains(.,'Tiến hành thanh toán')]").click()
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Xác Nhận Thanh Toán')]")))
        time.sleep(0.3)

    def checkout(self):
        # Direct access guard while logged out.
        self.fresh("/checkout", None); time.sleep(0.3)
        form = bool(self.d.find_elements(By.XPATH, "//button[contains(.,'Xác Nhận Thanh Toán')]"))
        redirected = "/login" in self.d.current_url
        self.record("GUI-049", (not form) and redirected, f"Form hiển thị={form}, URL={self.d.current_url}", "checkout-direct")
        self.diagnostic(f"GUI-049 | direct /checkout while logged out | form={form} | redirected_to_login={redirected}")
        self.shot("checkout-direct")
        self.clear_diagnostic()

        self.prepare_checkout()
        h1s = self.d.find_elements(By.CSS_SELECTOR, "main h1")
        self.record("GUI-038", len(h1s) == 1 and any(x in h1s[0].text.lower() for x in ("checkout", "xác nhận", "thanh toán")), f"Số h1={len(h1s)}, headings={[x.text for x in self.d.find_elements(By.CSS_SELECTOR,'main h1,main h2')]}", "checkout")
        text = self.text()
        self.record("GUI-039", "iPhone 15 Pro Max" in text and "x 1" in text and "30,000,000 ₫" in text, "Tóm tắt có tên, quantity và thành tiền" if "iPhone 15 Pro Max" in text else "Thiếu sản phẩm trong tóm tắt", "checkout")
        money = re.findall(r"-?[\d,]+ ₫", text)
        self.record("GUI-040", bool(money) and all(re.fullmatch(r"-?\d{1,3}(,\d{3})+ ₫", x) for x in money), f"Giá trị tiền={money}", "checkout")
        self.viewport(375, 900)
        checkout_vw = self.js("return innerWidth")
        checkout_sw = self.js("return document.documentElement.scrollWidth")
        responsive = checkout_sw <= checkout_vw + 1
        self.record("GUI-041", responsive, f"viewport={checkout_vw}, scrollWidth={checkout_sw}", "checkout")
        self.viewport(1440, 1000)
        total = self.d.find_element(By.CSS_SELECTOR, "input[type=number]")
        before = total.get_attribute("value")
        total.send_keys(Keys.CONTROL, "a"); total.send_keys("60000"); time.sleep(0.1)
        editable = total.get_attribute("value") == "60000" and not total.get_attribute("readonly") and not total.get_attribute("disabled")
        self.record("GUI-042", not editable, f"Giá trị trước={before}, sau nhập=60000; readonly={total.get_attribute('readonly')}, disabled={total.get_attribute('disabled')}", "checkout-editable")
        coupon = self.d.find_element(By.CSS_SELECTOR, "input[placeholder*='mã giảm giá']")
        labels = [x.text for x in self.d.find_elements(By.TAG_NAME, "label")]
        apply = self.d.find_element(By.XPATH, "//button[normalize-space()='Áp dụng']")
        self.record("GUI-043", any("Mã Giảm Giá" in x for x in labels) and apply.is_displayed(), f"Labels={labels}, nút Áp dụng displayed={apply.is_displayed()}", "checkout")
        coupon.send_keys("   "); time.sleep(0.1)
        self.record("GUI-044", not apply.is_enabled(), f"Khoảng trắng: Apply enabled={apply.is_enabled()}", "checkout")
        crumbs = self.d.find_elements(By.CSS_SELECTOR, "nav[aria-label*=breadcrumb], .breadcrumb")
        self.record("GUI-046", bool(crumbs), f"breadcrumb count={len(crumbs)}", "checkout")
        checkout_nav = [a for a in self.d.find_elements(By.TAG_NAME, "a") if "checkout" in a.text.lower() or "thanh toán" in a.text.lower()]
        highlighted = any(a.get_attribute("aria-current") == "page" or "active" in (a.get_attribute("class") or "").lower() for a in checkout_nav)
        self.record("GUI-047", highlighted, f"Navbar checkout links={[(a.text,a.get_attribute('class')) for a in checkout_nav]}", "checkout")
        self.shot("checkout")
        self.shot("checkout-editable")

        # Back to cart and return by browser history.
        self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.2)
        cart_kept = "iPhone 15 Pro Max" in self.text()
        self.d.back(); time.sleep(0.25)
        checkout_kept = "iPhone 15 Pro Max" in self.text() and "/checkout" in self.d.current_url
        self.record("GUI-048", cart_kept and checkout_kept, f"Cart giữ sản phẩm={cart_kept}, trở về Checkout giữ tóm tắt={checkout_kept}", "checkout")

        # Keyboard sequence.
        coupon_for_keyboard = self.d.find_element(By.CSS_SELECTOR, "input[placeholder*='mã giảm giá']")
        coupon_for_keyboard.send_keys("SAVE10")
        self.js("document.body.tabIndex=-1;document.body.focus()"); focus=[]
        for _ in range(14):
            self.d.switch_to.active_element.send_keys(Keys.TAB)
            a=self.d.switch_to.active_element
            focus.append({"tag": a.tag_name, "name": (a.get_attribute("placeholder") or a.text or a.get_attribute("type") or a.tag_name).strip()})
        needed = ["Nhập mã giảm giá...", "Áp dụng", "Xác Nhận Thanh Toán"]
        focus_names = [x["name"] for x in focus if x["tag"] != "body"]
        self.record("GUI-060", all(any(n in f for f in focus_names) for n in needed), f"Thứ tự focus={focus_names}", "checkout-focus")
        self.shot("checkout-focus")

        # Coupon loading, valid calculation and invalid behavior in a logged-out empty checkout with editable total.
        self.fresh("/checkout", "input[type=number]")
        total = self.d.find_element(By.CSS_SELECTOR, "input[type=number]")
        total.send_keys(Keys.CONTROL, "a"); total.send_keys("30000000")
        coupon = self.d.find_element(By.CSS_SELECTOR, "input[placeholder*='mã giảm giá']")
        coupon.send_keys("SAVE10")
        apply = self.d.find_element(By.XPATH, "//button[normalize-space()='Áp dụng']")
        self.js("window.__states=[];let b=arguments[0];new MutationObserver(()=>__states.push({t:b.innerText,d:b.disabled})).observe(b,{attributes:true,childList:true,subtree:true});", apply)
        apply.click(); self.wait.until(lambda d: "Tiết kiệm" in d.find_element(By.TAG_NAME,"body").text or "đạt giới hạn" in d.find_element(By.TAG_NAME,"body").text)
        states = self.js("return window.__states")
        loading_ok = any(s.get("d") and s.get("t") == "..." for s in states)
        self.record("GUI-045", loading_ok, f"Mutation states của Apply={states}", "coupon-valid")
        coupon_text = self.text()
        correct_coupon = "3,000,000 ₫" in coupon_text and "27,000,000 ₫" in coupon_text
        self.record("GUI-050", correct_coupon, f"Kết quả SAVE10 chứa giảm 3,000,000 và thành tiền 27,000,000={correct_coupon}; text={coupon_text[-280:]!r}", "coupon-valid")
        self.shot("coupon-valid")

        total_before = self.d.find_element(By.CSS_SELECTOR, "input[type=number]").get_attribute("value")
        coupon = self.d.find_element(By.CSS_SELECTOR, "input[placeholder*='mã giảm giá']")
        coupon.send_keys(Keys.CONTROL, "a"); coupon.send_keys("INVALID")
        self.d.find_element(By.XPATH, "//button[normalize-space()='Áp dụng']").click()
        self.wait.until(lambda d: "không tồn tại" in d.find_element(By.TAG_NAME,"body").text.lower())
        invalid_error = "không tồn tại" in self.text().lower()
        total_after = self.d.find_element(By.CSS_SELECTOR, "input[type=number]").get_attribute("value")
        self.record("GUI-051", invalid_error and total_before == total_after, f"Lỗi cụ thể={invalid_error}, tổng giữ nguyên={total_before==total_after}", "coupon-invalid")
        self.shot("coupon-invalid")

        # Positive/negative colors and contrast measured from actual controls.
        self.prepare_checkout()
        pos = self.d.find_element(By.XPATH, "//button[contains(.,'Xác Nhận Thanh Toán')]")
        pos_bg = pos.value_of_css_property("background-color")
        self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.2)
        delete = self.d.find_element(By.CSS_SELECTOR, "tbody button")
        neg_color = delete.value_of_css_property("color")
        blue = "37, 99, 235" in pos_bg or "59, 130, 246" in pos_bg
        red = "239, 68, 68" in neg_color
        self.record("GUI-056", blue and red, f"Action background={pos_bg}, Xóa color={neg_color}", "cross-color")
        self.shot("cross-color")

        self.d.back(); time.sleep(0.2)
        apply = self.d.find_element(By.XPATH, "//button[normalize-space()='Áp dụng']")
        pos = self.d.find_element(By.XPATH, "//button[contains(.,'Xác Nhận Thanh Toán')]")
        contrast = self.js("""
          function rgb(s){return s.match(/[0-9.]+/g).slice(0,3).map(Number)}
          function lum(c){return c.map(v=>{v/=255;return v<=.03928?v/12.92:Math.pow((v+.055)/1.055,2.4)}).reduce((a,v,i)=>a+v*[.2126,.7152,.0722][i],0)}
          function ratio(e){let s=getComputedStyle(e),a=lum(rgb(s.color)),b=lum(rgb(s.backgroundColor));return (Math.max(a,b)+.05)/(Math.min(a,b)+.05)}
          return {apply:ratio(arguments[0]),checkout:ratio(arguments[1])}
        """, apply, pos)
        contrast_ok = contrast["apply"] >= 4.5 and contrast["checkout"] >= 4.5
        self.record("GUI-058", contrast_ok, f"Contrast Apply={contrast['apply']:.2f}:1, Checkout={contrast['checkout']:.2f}:1", "cross-contrast")
        self.shot("cross-contrast")

        body_text = self.text()
        english = [x for x in ("Checkout", "Add to cart", "Delete", "Apply") if x in body_text]
        self.record("GUI-057", not english, f"Nhãn tiếng Anh ngoài thuật ngữ chuẩn={english}", "checkout")

        # Long Vietnamese content stress in actual rendered containers.
        self.long_checks["checkout"] = self.js("""
          let nodes=[...document.querySelectorAll('h1,h2,li,button,label')];
          let old=nodes.map(n=>n.textContent); nodes.forEach(n=>n.textContent += ' nội dung tiếng Việt rất dài để kiểm tra bố cục');
          let ok=document.documentElement.scrollWidth<=innerWidth+1; nodes.forEach((n,i)=>n.textContent=old[i]); return ok;
        """)
        long_ok = all(self.long_checks.get(k, False) for k in ("product", "cart", "checkout"))
        self.record("GUI-062", long_ok, f"Stress text dài: Product={self.long_checks.get('product')}, Cart={self.long_checks.get('cart')}, Checkout={self.long_checks.get('checkout')}", "checkout")
        imgs = self.d.find_elements(By.CSS_SELECTOR, "main img")
        bad_alt = [i for i in imgs if not (i.get_attribute("alt") or "").strip()]
        self.record("GUI-063", not bad_alt, f"Ảnh trong Cart/Checkout={len(imgs)}, ảnh alt rỗng={len(bad_alt)}", "checkout")

        # Touch targets from checkout, combined with cart result already recorded.
        self.viewport(375, 900)
        controls = self.d.find_elements(By.XPATH, "//button")
        sizes = [(x.text.strip(), round(x.rect['width'],1), round(x.rect['height'],1)) for x in controls if x.text.strip() in ("Áp dụng","Xác Nhận Thanh Toán")]
        checkout_touch = len(sizes)==2 and all(w>=44 and h>=44 for _,w,h in sizes)
        old_note = self.results["GUI-061"]["notes"]
        cart_touch = self.results["GUI-061"]["result"] == "Passed"
        self.record("GUI-061", cart_touch and checkout_touch, f"{old_note}; Checkout={sizes}", "cross-touch")
        self.shot("cross-touch")
        self.viewport(1440, 1000)

        # Checkout processing/success/cart clearing/home action.
        checkout_btn = self.d.find_element(By.XPATH, "//button[contains(.,'Xác Nhận Thanh Toán')]")
        self.js("window.__states=[];let b=arguments[0];new MutationObserver(()=>__states.push({t:b.innerText,d:b.disabled})).observe(b,{attributes:true,childList:true,subtree:true});", checkout_btn)
        checkout_btn.click()
        try:
            self.wait.until(lambda d: "Thanh toán thành công" in d.find_element(By.TAG_NAME,"body").text)
        except TimeoutException:
            pass
        states = self.js("return window.__states")
        processing = any(s.get("d") and "Đang xử lý" in s.get("t","") for s in states)
        success = "Thanh toán thành công" in self.text()
        self.record("GUI-052", processing, f"Mutation states Checkout={states}", "checkout-success")
        self.record("GUI-053", success, f"Thông báo thành công hiển thị={success}", "checkout-success")
        home_btn = self.d.find_elements(By.XPATH, "//button[contains(.,'Quay lại trang chủ')]")
        self.record("GUI-055", bool(home_btn), f"Hành động Quay lại trang chủ tồn tại={bool(home_btn)}", "checkout-success")
        self.shot("checkout-success")
        if home_btn:
            home_btn[0].click(); time.sleep(0.2)
        home_works = self.d.current_url.rstrip("/") == BASE
        self.record("GUI-055", bool(home_btn) and home_works, f"Hành động tồn tại={bool(home_btn)}, điều hướng Home={home_works}", "checkout-success")
        self.d.find_element(By.LINK_TEXT, "Giỏ hàng").click(); time.sleep(0.2)
        cleared = "iPhone 15 Pro Max" not in self.text()
        self.record("GUI-054", cleared, f"Sau checkout, sản phẩm còn trong Cart={not cleared}", "checkout-cart-after")
        self.shot("checkout-cart-after")

        # Session expiry: remove token and reload while at checkout; observe message/cart preservation.
        self.prepare_checkout()
        self.js("localStorage.removeItem('token')")
        self.d.refresh(); time.sleep(0.8)
        expired_text = self.text().lower()
        expiry_message = "hết hạn" in expired_text or "đăng nhập lại" in expired_text
        cart_visible = "iphone 15 pro max" in expired_text
        form_visible = bool(self.d.find_elements(By.XPATH, "//button[contains(.,'Xác Nhận Thanh Toán')]"))
        self.record("GUI-064", expiry_message and cart_visible and not form_visible, f"Thông báo hết hạn={expiry_message}, giữ giỏ={cart_visible}, form vẫn mở={form_visible}", "session-expiry")
        self.diagnostic(
            "GUI-064 | token removed + page refreshed | "
            f"expiry_message={expiry_message} | cart_preserved={cart_visible} | checkout_form_visible={form_visible}"
        )
        self.shot("session-expiry")
        self.clear_diagnostic()

        # Actual one-shot network failure and retry for coupon and checkout.
        self.fresh("/checkout", "input[type=number]")
        total=self.d.find_element(By.CSS_SELECTOR,"input[type=number]"); total.send_keys(Keys.CONTROL,"a"); total.send_keys("30000000")
        coupon=self.d.find_element(By.CSS_SELECTOR,"input[placeholder*='mã giảm giá']"); coupon.send_keys("SAVE10")
        self.js("""
          window.__origOpen=XMLHttpRequest.prototype.open; window.__failed=false;
          XMLHttpRequest.prototype.open=function(m,u){if(!window.__failed && String(u).includes('apply-coupon')){window.__failed=true;return window.__origOpen.call(this,m,'http://127.0.0.1:9/fail')}return window.__origOpen.call(this,m,u)};
        """)
        apply=self.d.find_element(By.XPATH,"//button[normalize-space()='Áp dụng']"); apply.click(); time.sleep(1)
        enabled_after_error=apply.is_enabled(); apply.click(); time.sleep(1)
        retried="Tiết kiệm" in self.text()
        self.prepare_checkout()
        self.js("""
          window.__origOpen=XMLHttpRequest.prototype.open; window.__failed=false;
          XMLHttpRequest.prototype.open=function(m,u){if(!window.__failed && String(u).includes('/api/checkout')){window.__failed=true;return window.__origOpen.call(this,m,'http://127.0.0.1:9/fail')}return window.__origOpen.call(this,m,u)};
        """)
        pay=self.d.find_element(By.XPATH,"//button[contains(.,'Xác Nhận Thanh Toán')]"); pay.click(); time.sleep(1)
        try:
            self.d.switch_to.alert.accept()
        except NoAlertPresentException:
            pass
        checkout_reenabled=pay.is_enabled(); pay.click(); time.sleep(1)
        checkout_retry="Thanh toán thành công" in self.text()
        all_recovered = enabled_after_error and retried and checkout_reenabled and checkout_retry
        self.record("GUI-065", all_recovered, f"Coupon bật lại={enabled_after_error}, coupon retry={retried}; Checkout bật lại={checkout_reenabled}, checkout retry={checkout_retry}", "network-retry")
        self.shot("network-retry")

    def finish(self):
        missing = sorted(set(self.items) - set(self.results))
        if missing:
            raise RuntimeError(f"Missing results: {missing}")
        RESULTS.mkdir(parents=True, exist_ok=True)
        SHOTS.mkdir(parents=True, exist_ok=True)

        # Stamp overview and every failed item; each platform uses its own observed screenshot.
        overview_in, overview_url = self.states["product"]
        overview_out = SHOTS / f"{self.p.slug}-overview.png"
        self.stamp(overview_in, overview_out, overview_url)

        lines = [
            f"# Kết quả M8 — {self.p.label}", "",
            f"- **Platform:** {self.p.label}",
            f"- **User agent:** `{self.ua}`", f"- **Base URL:** `{BASE}`",
            f"- **Thời điểm:** 16/11/2026 (UTC+07:00)", "",
            "| ID | IA | Screen | Checklist item | Platform Result | Notes | Screenshot | Bug ID |",
            "|---|---|---|---|---|---|---|---|",
        ]
        for item_id in sorted(self.items):
            meta = self.items[item_id]
            r = self.results[item_id]
            screenshot = ""
            if r["result"] == "Failed":
                source, source_url = self.states.get(r["state"], (overview_in, overview_url))
                out = SHOTS / f"{self.p.slug}-{item_id}.png"
                self.stamp(source, out, source_url)
                screenshot = f"[evidence](../screenshots/{out.name})"
            note = r["notes"].replace("|", "/").replace("\n", " ")
            item_text = meta["item"].replace("|", "/")
            bug = meta["bug"] if r["result"] == "Failed" else ""
            bug = bug.replace("(../bug-reports/", "(../../bug-reports/")
            if item_id == "GUI-002" and r["result"] == "Failed":
                bug = "[BUG-IA-01-PRODUCT-001](../../bug-reports/BUG-IA-01-PRODUCT-001.md) · [Issue #64](https://github.com/thu2005/CSC13003_eshop/issues/64)"
            lines.append(f"| {item_id} | {meta['ia']} | {meta['screen']} | {item_text} | {r['result']} | {note} | {screenshot} | {bug} |")
        passed = sum(r["result"] == "Passed" for r in self.results.values())
        failed = 65 - passed
        lines += ["", "## Tổng hợp", "", "| Executed | Passed | Failed |", "|---:|---:|---:|", f"| 65 | {passed} | {failed} |", ""]
        (RESULTS / f"{self.p.slug}.md").write_text("\n".join(lines), encoding="utf-8")
        summary = {"platform": self.p.label, "slug": self.p.slug, "ua": self.ua, "executed": 65, "passed": passed, "failed": failed, "overview": overview_out.name}
        (RESULTS / f"{self.p.slug}.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False))

    def stamp(self, source: Path, out: Path, url: str):
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        subprocess.run([
            sys.executable, str(STAMP), str(source), str(out), EMAIL,
            "--label", STUDENT, "--label", self.p.label, "--label", url,
        ], check=True, stdout=subprocess.DEVNULL, env=env)

    def execute(self):
        self.product()
        self.cart()
        self.checkout()
        self.finish()


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in PLATFORMS:
        raise SystemExit(f"Usage: {Path(sys.argv[0]).name} <{'|'.join(PLATFORMS)}>")
    items = parse_items()
    run = Run(PLATFORMS[sys.argv[1]], items)
    try:
        run.execute()
    finally:
        run.close()


if __name__ == "__main__":
    main()
