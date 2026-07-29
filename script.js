/* EmailJS — 문의하기 템플릿 */
const EMAILJS_SERVICE_ID = "allbarunclean";
const EMAILJS_TEMPLATE_ID = "template_b4ox5js";
const EMAILJS_PUBLIC_KEY = "JKsVOKPtnWHIr2BCV";

/* 이벤트 내용이 정해지면 true로 바꾸고 팝업 문구를 수정하세요 */
const EVENT_POPUP_ENABLED = false;
const EVENT_POPUP_STORAGE_KEY = "refreshhome_gimhae_event_hide_today";

(function initEmailJS() {
  if (window.emailjs && EMAILJS_PUBLIC_KEY) {
    emailjs.init({ publicKey: EMAILJS_PUBLIC_KEY });
  }
})();

document.addEventListener("DOMContentLoaded", () => {
  setupNav();
  setupSymptoms();
  setupConsultForms();
  setupEventPopup();
  if (typeof setupReviews === "function") setupReviews();
});

function setupNav() {
  const nav = document.querySelector(".nav");
  const toggle = document.querySelector(".navToggle");
  if (!nav || !toggle) return;

  toggle.addEventListener("click", () => {
    const open = nav.classList.toggle("menu-open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
  });

  nav.querySelectorAll(".navlinks a").forEach((link) => {
    link.addEventListener("click", () => {
      nav.classList.remove("menu-open");
      toggle.setAttribute("aria-expanded", "false");
    });
  });
}

function setupSymptoms() {
  const buttons = document.querySelectorAll("[data-symptom]");
  const hint = document.getElementById("symptomHint");
  if (!buttons.length) return;

  buttons.forEach((btn) => {
    btn.addEventListener("click", () => {
      btn.classList.toggle("active");
      const any = [...buttons].some((b) => b.classList.contains("active"));
      if (hint) hint.hidden = !any;
    });
  });
}

function setupConsultForms() {
  const forms = document.querySelectorAll(".consultForm");

  forms.forEach((form) => {
    form.addEventListener("submit", async (e) => {
      e.preventDefault();

      const status = form.querySelector(".status");
      const btn = form.querySelector('button[type="submit"]');

      status.textContent = "";
      status.className = "status";

      const agree = form.querySelector('input[name="agree"]');
      if (!agree || !agree.checked) {
        status.textContent = "개인정보 수집 및 이용에 동의해 주세요.";
        status.classList.add("err");
        return;
      }

      const data = Object.fromEntries(new FormData(form).entries());

      if (!data.name || !data.phone || !data.address) {
        status.textContent = "성함, 연락처, 현장 주소를 입력해 주세요.";
        status.classList.add("err");
        return;
      }

      if (!window.emailjs) {
        status.textContent = "접수 설정이 아직 연결되지 않았습니다. 전화 상담(010-4026-0892)을 이용해 주세요.";
        status.classList.add("err");
        return;
      }

      btn.disabled = true;
      btn.textContent = "접수 중입니다...";

      const messageText = `사이트 : ${data.site_name || "리프레시홈 김해"}
지역 : ${data.region || "김해"}

연락처 : ${data.phone}

서비스 : ${data.service}

주소 : ${data.address}

상담내용 :
${data.message || ""}

접수시간 :
${new Date().toLocaleString("ko-KR")}`;

      try {
        await emailjs.send(EMAILJS_SERVICE_ID, EMAILJS_TEMPLATE_ID, {
          from_name: data.name,
          name: data.name,
          phone: data.phone,
          region: `${data.region || "김해"} / ${data.address}`,
          service: data.service,
          message: messageText
        });

        status.textContent = "예약 접수가 완료되었습니다. 확인 후 연락드리겠습니다.";
        status.classList.add("ok");
        form.reset();
      } catch (err) {
        console.error("EmailJS Error:", err);
        status.textContent = "접수 중 오류가 발생했습니다. 전화 상담을 이용해 주세요.";
        status.classList.add("err");
      } finally {
        btn.disabled = false;
        btn.textContent = "예약 접수하기";
      }
    });
  });
}

function setupEventPopup() {
  const popup = document.getElementById("eventPopup");
  if (!popup || !EVENT_POPUP_ENABLED) return;

  if (isHiddenToday()) return;

  popup.hidden = false;
  popup.setAttribute("aria-hidden", "false");
  document.body.style.overflow = "hidden";

  popup.querySelectorAll("[data-close-popup]").forEach((el) => {
    el.addEventListener("click", () => closePopup(popup));
  });

  const hideToday = popup.querySelector("[data-hide-today]");
  if (hideToday) {
    hideToday.addEventListener("click", () => {
      localStorage.setItem(EVENT_POPUP_STORAGE_KEY, todayKey());
      closePopup(popup);
    });
  }
}

function closePopup(popup) {
  popup.hidden = true;
  popup.setAttribute("aria-hidden", "true");
  document.body.style.overflow = "";
}

function todayKey() {
  const d = new Date();
  return `${d.getFullYear()}-${d.getMonth() + 1}-${d.getDate()}`;
}

function isHiddenToday() {
  try {
    return localStorage.getItem(EVENT_POPUP_STORAGE_KEY) === todayKey();
  } catch {
    return false;
  }
}
