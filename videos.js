/**
 * 작업 영상 렌더링
 * - 데이터: data/videos.json
 * - 추가 방법: JSON 맨 위에 항목을 넣고 youtube 영상 ID만 적기
 *
 * 필드 예시
 * {
 *   "id": "uPZAKHprA7U",
 *   "youtube": "uPZAKHprA7U",
 *   "title": "리프레쉬 홈 매트리스청소",
 *   "text": "짧은 설명"
 * }
 */

const VIDEOS_JSON_URL = "/data/videos.json";
const HOME_VIDEO_LIMIT = 1;

function escapeVideoHtml(value) {
  return String(value || "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function youtubeId(value) {
  const raw = String(value || "").trim();
  if (!raw) return "";
  const match = raw.match(/(?:youtu\.be\/|v=|embed\/)([A-Za-z0-9_-]{6,})/);
  return match ? match[1] : raw;
}

function videoCardHtml(item) {
  const id = youtubeId(item.youtube || item.id);
  if (!id) return "";
  const title = escapeVideoHtml(item.title || "작업 영상");
  const text = escapeVideoHtml(item.text || "");

  return `<article class="videoCard">
    <div class="videoFrame">
      <iframe
        src="https://www.youtube-nocookie.com/embed/${escapeVideoHtml(id)}"
        title="${title}"
        loading="lazy"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        referrerpolicy="strict-origin-when-cross-origin"
        allowfullscreen></iframe>
    </div>
    <h3>${title}</h3>
    ${text ? `<p>${text}</p>` : ""}
  </article>`;
}

async function loadVideos() {
  const res = await fetch(VIDEOS_JSON_URL, { cache: "no-store" });
  if (!res.ok) throw new Error("영상 데이터를 불러오지 못했습니다.");
  const data = await res.json();
  return Array.isArray(data) ? data : [];
}

async function setupVideos() {
  const homeList = document.getElementById("videoList");
  const fullList = document.getElementById("videoListAll");
  const target = fullList || homeList;
  if (!target) return;

  try {
    const videos = await loadVideos();
    const items = fullList ? videos : videos.slice(0, HOME_VIDEO_LIMIT);

    if (!items.length) {
      target.innerHTML = `<p class="reviewEmpty">등록된 작업 영상이 없습니다.</p>`;
      return;
    }

    target.innerHTML = items.map(videoCardHtml).join("");
  } catch (err) {
    console.error(err);
    target.innerHTML = `<p class="reviewEmpty">영상을 불러오는 중 문제가 발생했습니다.</p>`;
  }
}
