#!/usr/bin/env python3
"""index.html -> graph-embed.html (노션 임베드용 지식 그래프 단독 페이지) 생성기.

index.html 을 고친 뒤 `python3 build-embed.py` 로 재생성한다.
"""
import io

EMBED = '''
<style id="embed-mode">
/* ===== Notion 임베드 전용: 지식 그래프만 표시 ===== */
nav, header.hero, #about, #schedule, #casebook, #map, #news, footer { display:none !important; }

/* 프레임 높이에 정확히 맞춰서 내부 스크롤이 생기지 않게 한다 */
html, body { margin:0; padding:0; height:100%; overflow:hidden; background:#07130D; }

#graph { padding:0 !important; margin:0 !important; height:100%; min-height:0; display:flex; align-items:stretch; }
#graph .container {
  max-width:100% !important; width:100%; height:100%; min-height:0;
  padding:14px 16px 16px !important; display:flex; flex-direction:column;
}

/* 섹션 라벨/제목/설명은 임베드에서 불필요 */
#graph .sec-label, #graph .sec-title, #graph .sec-desc { display:none !important; }

/* 검색은 가운데 크게 유지하되 위아래 여백만 압축 */
#graph .gsearchbar { margin:4px auto 6px !important; flex:none; }
#graph .gcount { margin-top:6px !important; flex:none; }
#graph .gtags { margin:8px 0 10px !important; flex:none; }
#graph .glegend { margin-top:10px !important; flex:none; }

/* 그래프 캔버스가 남는 높이를 모두 차지 */
#graph .graph-shell { flex:1 1 auto; min-height:0; height:auto !important; }

/* ---------- 모바일: 스크롤 없이 한 화면에 ---------- */
@media (max-width:640px){
  #graph .container { padding:10px 10px 10px !important; }

  /* 검색창 축소 */
  #graph .gsearchbar { max-width:100%; gap:6px; margin:0 auto 6px !important; }
  #graph .gsearchbar input { padding:11px 14px !important; font-size:14px !important; border-radius:11px; }
  #graph .gsearchbar .btn { padding:11px 15px !important; font-size:13px !important; border-radius:11px; }

  /* 태그: 여러 줄로 쌓이지 않게 한 줄 가로 스크롤 */
  #graph .gtags {
    flex-wrap:nowrap !important; overflow-x:auto; justify-content:flex-start;
    margin:0 0 6px !important; padding-bottom:2px;
    scrollbar-width:none; -webkit-overflow-scrolling:touch;
  }
  #graph .gtags::-webkit-scrollbar { display:none; }
  #graph .gtag { flex:none; }

  /* 개수 표시와 범례는 공간을 많이 먹어 숨김 */
  #graph .gcount, #graph .glegend { display:none !important; }

  /* 그래프 위 / 정보 패널 아래로 나누고, 남는 높이를 비율로 분배 */
  #graph .graph-shell {
    grid-template-columns:1fr !important;
    grid-template-rows:1fr minmax(110px, 38%) !important;
  }
  #graph #gnet { height:auto !important; min-height:0; }
  #graph #gpanel { max-height:none !important; padding:14px !important; }
  #graph #gpanel .empty { margin-top:12px; font-size:12.5px; }
}
</style>

<base target="_blank">
</head>'''


def main():
    s = io.open("index.html", encoding="utf-8").read()
    s = s.replace("<title>Physical AI Hackathon — LG인화원 MBA</title>",
                  "<title>Physical AI 지식 그래프</title>", 1)
    assert s.count("</head>") == 1, "</head> 가 하나여야 합니다"
    s = s.replace("</head>", EMBED.split("</head>")[0] + "</head>", 1)
    io.open("graph-embed.html", "w", encoding="utf-8").write(s)
    print("graph-embed.html 생성 완료")


if __name__ == "__main__":
    main()
