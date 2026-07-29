/**
 * 작업후기 렌더링
 * - 데이터: data/reviews.json
 * - 추가 방법: JSON에 항목을 위에 추가하고, 사진은 images/reviews/ 에 넣기
 *
 * 필드 예시
 * {
 *   "id": "2026-07-29-jangyu",
 *   "date": "2026-07-29",
 *   "area": "장유",
 *   "service": "매트리스 클리닝",
 *   "title": "김해 장유 매트리스 클리닝",
 *   "text": "짧은 후기 문구",
 *   "name": "김○○",
 *   "before": "images/reviews/2026-07-29-before.jpg",
 *   "after": "images/reviews/2026-07-29-after.jpg"
 * }
 */

const REVIEWS_JSON_URL = "/data/reviews.json";
const HOME_REVIEW_LIMIT = 6;

function escapeHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function formatDate(dateStr) {
  if (!dateStr) return "";
  const d = new Date(dateStr);
  if (Number.isNaN(d.getTime())) return dateStr;
  return `${d.getFullYear()}.${String(d.getMonth() + 1).padStart(2, "0")}.${String(d.getDate()).padStart(2, "0")}`;
}

function reviewCardHtml(item) {
  const title = escapeHtml(item.title || `${item.area || ""} ${item.service || ""}`.trim());
  const text = escapeHtml(item.text);
  const area = escapeHtml(item.area);
  const service = escapeHtml(item.service);
  const name = escapeHtml(item.name || "고객님");
  const date = escapeHtml(formatDate(item.date));
  const before = item.before ? escapeHtml(item.before) : "";
  const after = item.after ? escapeHtml(item.after) : "";

  let photos = "";
  if (before || after) {
    photos = `<div class="reviewPhotos">`;
    if (before) {
      photos += `<figure><span class="baLabel">BEFORE</span><img src="${before}" alt="${title} 작업 전" loading="lazy"></figure>`;
    }
    if (after) {
      photos += `<figure><span class="baLabel after">AFTER</span><img src="${after}" alt="${title} 작업 후" loading="lazy"></figure>`;
    }
    photos += `</div>`;
  }

  return `<article class="reviewCard">
    <div class="reviewMeta">
      <span class="reviewService">${service}</span>
      ${date ? `<time datetime="${escapeHtml(item.date)}">${date}</time>` : ""}
    </div>
    <h3>${title}</h3>
    ${photos}
    <p>${text}</p>
    <footer>${name}${area ? ` · ${area}` : ""}</footer>
  </article>`;
}

async function loadReviews() {
  const res = await fetch(REVIEWS_JSON_URL, { cache: "no-store" });
  if (!res.ok) throw new Error("후기 데이터를 불러오지 못했습니다.");
  const data = await res.json();
  if (!Array.isArray(data)) return [];
  return data.slice().sort((a, b) => String(b.date || "").localeCompare(String(a.date || "")));
}

async function setupReviews() {
  const homeList = document.getElementById("reviewList");
  const fullList = document.getElementById("reviewListAll");
  const target = fullList || homeList;
  if (!target) return;

  try {
    const reviews = await loadReviews();
    const items = fullList ? reviews : reviews.slice(0, HOME_REVIEW_LIMIT);

    if (!items.length) {
      target.innerHTML = `<p class="reviewEmpty">등록된 작업후기가 없습니다.</p>`;
      return;
    }

    target.innerHTML = items.map(reviewCardHtml).join("");

    const countEl = document.getElementById("reviewCount");
    if (countEl) countEl.textContent = `총 ${reviews.length}건`;
  } catch (err) {
    console.error(err);
    target.innerHTML = `<p class="reviewEmpty">후기를 불러오는 중 문제가 발생했습니다.</p>`;
  }
}
