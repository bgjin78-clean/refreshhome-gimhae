# -*- coding: utf-8 -*-
"""김해 하위 지역 SEO 페이지 생성"""
from pathlib import Path
from datetime import date

BASE = "https://www.gimhae.refreshhome.co.kr"
PHONE = "010-4026-0892"
TODAY = date.today().isoformat()
ROOT = Path(__file__).resolve().parent.parent
AREAS_DIR = ROOT / "areas"

# (이름, slug, 지역 특성 한 줄)
AREAS = [
    ("장유", "jangyu", "신도시 아파트·빌라가 많아 매트리스·소파 정기 클리닝 문의가 많은 지역입니다."),
    ("장유1동", "jangyu1", "관동·대청 일대 주거밀집 지역으로 침대·소파 출장 청소 상담이 이어집니다."),
    ("장유2동", "jangyu2", "계룡·내덕 일대 아파트 단지가 많아 매트리스냄새제거 요청이 많습니다."),
    ("장유3동", "jangyu3", "부곡·삼문 일대 신축·기존 주택이 섞여 침대개오줌냄새제거 상담도 많습니다."),
    ("내외동", "naeoe", "김해 시내권으로 접근이 좋아 당일·익일 매트리스청소 예약이 가능합니다."),
    ("삼계동", "samgye", "대단지 아파트와 주택이 함께 있어 소파·매트리스 동시 클리닝 문의가 많습니다."),
    ("부원동", "buwon", "구도심 주거지역으로 오래된 매트리스·침대 냄새 케어 상담이 이어집니다."),
    ("활천동", "hwalcheon", "시내 인접 주거지로 빠른 출장 침대청소·소파청소가 가능합니다."),
    ("불암동", "buram", "생활권 중심 지역으로 반려동물 가정 개오줌냄새제거 문의가 있습니다."),
    ("대청동", "daecheong", "장유와 가까운 주거지역으로 매트리스청소·소파클리닝 출장을 안내합니다."),
    ("칠산서부동", "chilsanseobu", "주거·근린생활시설이 섞인 지역으로 침대·소파 케어 상담이 가능합니다."),
    ("회현동", "hoehyeon", "시내권 주택·아파트 밀집 지역으로 매트리스냄새제거 요청이 많습니다."),
    ("동상동", "dongsang", "구도심 생활권으로 오래된 매트리스·쇼파 클리닝 상담을 안내합니다."),
    ("북부동", "bukbu", "주거밀집 지역으로 김해 침대청소·소파청소 출장이 가능합니다."),
    ("삼안동", "saman", "시내 인접 생활권으로 매트리스·소파 당일 상담 요청이 이어집니다."),
    ("진영읍", "jinyeong", "읍내·아파트 단지가 함께 있어 매트리스청소·소파청소 출장 상담이 가능합니다."),
    ("주촌면", "juchon", "산업단지·주거가 인접해 출장 침대청소·냄새제거 상담을 안내합니다."),
    ("진례면", "jinrye", "면 단위 주거지역으로 매트리스·소파 방문 클리닝이 가능합니다."),
    ("한림면", "hallim", "한림 일대 주택·아파트를 대상으로 매트리스청소 출장을 진행합니다."),
    ("생림면", "saengnim", "생림 지역 가정집 침대·소파 클리닝과 냄새제거를 안내합니다."),
    ("상동면", "sangdong", "상동 일대 출장으로 매트리스냄새제거·소파청소 상담이 가능합니다."),
    ("대동면", "daedong", "대동 지역 주택·아파트를 대상으로 침대청소·소파클리닝을 안내합니다."),
]


def nearby_links(current_slug, limit=6):
    others = [a for a in AREAS if a[1] != current_slug]
    # rotate based on index for variety
    idx = next(i for i, a in enumerate(AREAS) if a[1] == current_slug)
    rotated = others[idx:] + others[:idx]
    return rotated[:limit]


def page_html(name, slug, note):
    title = f"{name} 매트리스청소 · 침대청소 · 소파청소 | 리프레시홈 김해"
    desc = (
        f"{name} 매트리스청소, 매트리스냄새제거, 침대청소, 개오줌냄새제거, 소파청소 출장. "
        f"리프레시홈 김해 {PHONE}"
    )
    nearby = nearby_links(slug)
    nearby_html = "\n".join(
        f'          <li><a href="/areas/{s}.html">{n} 매트리스청소</a></li>'
        for n, s, _ in nearby
    )

    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="keywords" content="{name} 매트리스청소, {name} 매트리스냄새제거, {name} 침대청소, {name} 개오줌냄새제거, {name} 소파청소, 김해 매트리스청소, 리프레시홈 김해">
  <meta name="robots" content="index,follow">
  <link rel="canonical" href="{BASE}/areas/{slug}.html">
  <link rel="icon" href="/favicon.ico" sizes="any">
  <link rel="icon" type="image/png" href="/favicon-32.png" sizes="32x32">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{desc}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{BASE}/areas/{slug}.html">
  <meta property="og:image" content="{BASE}/images/hero.png">
  <meta property="og:locale" content="ko_KR">
  <meta name="twitter:card" content="summary_large_image">
  <link rel="stylesheet" as="style" crossorigin href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable.min.css">
  <link rel="stylesheet" href="/style.css">
  <script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js"></script>
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "{name} 매트리스청소 · 소파청소",
    "serviceType": ["매트리스청소", "매트리스냄새제거", "침대청소", "개오줌냄새제거", "소파청소"],
    "provider": {{
      "@type": "LocalBusiness",
      "name": "리프레시홈 김해",
      "telephone": "{PHONE}",
      "url": "{BASE}/"
    }},
    "areaServed": {{
      "@type": "Place",
      "name": "김해시 {name}"
    }},
    "url": "{BASE}/areas/{slug}.html"
  }}
  </script>
</head>
<body>
  <header class="topbar">
    <div class="container nav">
      <a class="logo" href="/">리프레시홈 <span>김해</span></a>
      <nav class="navlinks" aria-label="주요 메뉴">
        <a href="/#services">서비스</a>
        <a href="/#price">가격</a>
        <a href="/#process">과정</a>
        <a href="/reviews/">후기</a>
        <a href="/#areas">지역</a>
        <a href="#consult">예약접수</a>
      </nav>
      <a class="call" href="tel:{PHONE}">{PHONE}</a>
      <button class="navToggle" type="button" aria-label="메뉴 열기" aria-expanded="false">
        <span></span><span></span><span></span>
      </button>
    </div>
  </header>

  <main>
    <section class="hero areaHero">
      <div class="heroBg" aria-hidden="true">
        <img src="/images/hero.png" alt="{name} 매트리스청소 전문 클리닝" width="1600" height="900" fetchpriority="high">
      </div>
      <div class="container heroInner">
        <p class="brandMark">리프레시홈 김해 · {name}</p>
        <h1>{name} 매트리스청소<br>침대·소파 전문 클리닝</h1>
        <p class="heroLead">{name} 매트리스냄새제거 · 개오줌냄새제거 · 소파청소 출장 케어</p>
        <div class="heroBtns">
          <a class="btn primary" href="tel:{PHONE}">전화상담 {PHONE}</a>
          <a class="btn secondary" href="#consult">예약접수</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow">AREA</p>
        <h2>{name} 매트리스·소파 청소</h2>
        <p class="lead">{note}</p>
        <div class="seoGrid">
          <article>
            <h3>{name} 매트리스청소</h3>
            <p>진드기·먼지·세균이 쌓인 매트리스를 건식·습식 딥클리닝으로 관리합니다.</p>
          </article>
          <article>
            <h3>{name} 매트리스냄새제거</h3>
            <p>땀·습기·생활 냄새를 흡입·살균·피톤치드 케어로 줄여드립니다.</p>
          </article>
          <article>
            <h3>{name} 침대청소</h3>
            <p>매트리스와 프레임 주변까지 함께 청소해 침대를 쾌적하게 만듭니다.</p>
          </article>
          <article>
            <h3>{name} 개오줌냄새제거</h3>
            <p>침대·매트리스에 밴 반려동물 소변 냄새를 현장 확인 후 맞춤 케어합니다.</p>
          </article>
          <article>
            <h3>{name} 소파청소</h3>
            <p>패브릭 소파의 얼룩·털·냄새까지 인원별 클리닝으로 관리합니다.</p>
          </article>
          <article>
            <h3>{name} 쇼파 클리닝</h3>
            <p>생활 오염이 많은 쇼파도 항균·탈취 케어로 깨끗하게 마무리합니다.</p>
          </article>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow">PROCESS</p>
        <h2>{name} 8단계 딥클리닝</h2>
        <p class="lead">전문 장비로 매트리스 깊숙한 진드기·냄새까지 제거합니다.</p>
        <ol class="processGrid">
          <li><img src="/images/step-01.png" alt="오염도 측정" width="640" height="640" loading="lazy"><span class="num">01</span><h3>오염도 측정</h3><p>현재 오염 상태를 직접 확인</p></li>
          <li><img src="/images/step-02.png" alt="프레임 주변 청소" width="640" height="640" loading="lazy"><span class="num">02</span><h3>프레임 주변 청소</h3><p>프레임 및 주변부 먼지 제거</p></li>
          <li><img src="/images/step-03.png" alt="건식 진공 청소" width="640" height="640" loading="lazy"><span class="num">03</span><h3>건식 진공 청소</h3><p>깊숙한 먼지·진드기 제거</p></li>
          <li><img src="/images/step-04.png" alt="고온 스팀 살균" width="640" height="640" loading="lazy"><span class="num">04</span><h3>고온 스팀 살균</h3><p>99% 살균 효과</p></li>
          <li><img src="/images/step-05.png" alt="오염물 확인" width="640" height="640" loading="lazy"><span class="num">05</span><h3>오염물 확인</h3><p>청소 후 결과를 현미경으로 확인</p></li>
          <li><img src="/images/step-06.png" alt="항균 케어" width="640" height="640" loading="lazy"><span class="num">06</span><h3>항균 케어</h3><p>세균 재번식 방지</p></li>
          <li><img src="/images/step-07.png" alt="피톤치드 소독" width="640" height="640" loading="lazy"><span class="num">07</span><h3>피톤치드 소독</h3><p>자연 항균·탈취 효과</p></li>
          <li><img src="/images/step-08.png" alt="진드기 시트" width="640" height="640" loading="lazy"><span class="num">08</span><h3>진드기 시트</h3><p>진드기 시트 부착</p></li>
        </ol>
        <div class="reviewMore">
          <a class="btn secondary dark" href="/#price">가격 알아보기</a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="container">
        <p class="eyebrow">NEARBY</p>
        <h2>{name} 인근 지역 바로가기</h2>
        <p class="lead">김해 다른 동·읍·면 매트리스청소 페이지입니다.</p>
        <ul class="areaList">
{nearby_html}
          <li><a href="/#areas">김해 전체 지역</a></li>
        </ul>
      </div>
    </section>

    <section class="section consult" id="consult">
      <div class="container">
        <div class="formWrap">
          <p class="eyebrow">RESERVE</p>
          <h2>{name} 매트리스·소파청소 예약</h2>
          <p class="lead">{name} 주소와 희망 서비스를 남겨 주세요. 확인 후 연락드립니다.</p>
          <form class="consultForm">
            <input type="hidden" name="title" value="[리프레시홈 김해] {name} 예약접수">
            <input type="hidden" name="site_name" value="리프레시홈 김해">
            <input type="hidden" name="region" value="김해 {name}">
            <div class="formGrid">
              <div class="field">
                <label for="name">성함</label>
                <input id="name" name="name" placeholder="예: 홍길동" autocomplete="name" required>
              </div>
              <div class="field">
                <label for="phone">연락처</label>
                <input id="phone" name="phone" placeholder="예: 010-0000-0000" autocomplete="tel" required>
              </div>
              <div class="field">
                <label for="service">요청 서비스</label>
                <select id="service" name="service">
                  <option value="매트리스청소">매트리스청소</option>
                  <option value="매트리스냄새제거">매트리스냄새제거</option>
                  <option value="침대청소">침대청소</option>
                  <option value="개오줌냄새제거">개오줌냄새제거</option>
                  <option value="소파청소">소파청소</option>
                  <option value="매트리스+소파">매트리스+소파</option>
                  <option value="기타 상담">기타 상담</option>
                </select>
              </div>
              <div class="field">
                <label for="address">현장 주소</label>
                <input id="address" name="address" placeholder="예: 김해 {name}" value="김해 {name}" required>
              </div>
              <div class="field full">
                <label for="message">상담 내용</label>
                <textarea id="message" name="message" rows="4" placeholder="매트리스 사이즈, 소파 인원, 희망 일정 등을 남겨 주세요."></textarea>
              </div>
            </div>
            <label class="agree">
              <input type="checkbox" name="agree" value="yes">
              <span>상담 안내를 위한 개인정보 수집 및 이용에 동의합니다.</span>
            </label>
            <button class="btn primary submitBtn" type="submit">예약 접수하기</button>
            <div class="status" aria-live="polite"></div>
          </form>
          <div class="consultAlt">
            <a class="altLink" href="tel:{PHONE}"><strong>전화 상담</strong><span>{PHONE}</span></a>
            <a class="altLink" href="https://open.kakao.com/o/sig1WPki" target="_blank" rel="noopener noreferrer"><strong>카카오톡 상담</strong><span>오픈채팅 · 24시간 접수</span></a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container">
      <strong>리프레시홈 김해 · {name}</strong>
      <p>{name} 매트리스청소 · 매트리스냄새제거 · 침대청소 · 개오줌냄새제거 · 소파청소</p>
      <p>상담전화 <a href="tel:{PHONE}">{PHONE}</a></p>
      <p class="copy">© 2026 리프레시홈 김해. All rights reserved.</p>
    </div>
  </footer>

  <div class="mobileQuick">
    <a href="tel:{PHONE}">전화상담</a>
    <a href="#consult">예약접수</a>
  </div>

  <script src="/script.js"></script>
</body>
</html>
"""


def main():
    AREAS_DIR.mkdir(parents=True, exist_ok=True)

    for name, slug, note in AREAS:
        path = AREAS_DIR / f"{slug}.html"
        path.write_text(page_html(name, slug, note), encoding="utf-8")
        print(f"wrote {path.name}")

    # sitemap
    urls = [
        ("/", "1.0"),
        ("/reviews/", "0.8"),
    ] + [(f"/areas/{slug}.html", "0.7") for _, slug, _ in AREAS]

    sitemap = ['<?xml version="1.0" encoding="UTF-8"?>',
               '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, priority in urls:
        sitemap.append("  <url>")
        sitemap.append(f"    <loc>{BASE}{loc}</loc>")
        sitemap.append(f"    <lastmod>{TODAY}</lastmod>")
        sitemap.append("    <changefreq>weekly</changefreq>")
        sitemap.append(f"    <priority>{priority}</priority>")
        sitemap.append("  </url>")
    sitemap.append("</urlset>")
    sitemap.append("")
    (ROOT / "sitemap.xml").write_text("\n".join(sitemap), encoding="utf-8")
    print("wrote sitemap.xml")
    print("done", len(AREAS), "areas")


if __name__ == "__main__":
    main()
