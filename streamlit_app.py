import streamlit as st
import base64

# --- 페이지 기본 설정 ---
st.set_page_config(
    page_title="한국 뮤지컬 대백과",
    page_icon="🎭",
    layout="wide"
)

# --- 세련된 배경과 커스텀 스타일 적용 ---
st.markdown("""
<style>
/* Streamlit 앱의 메인 배경 */
.stApp {
    background-image: linear-gradient(135deg, #1a2a6c, #000000);
    background-attachment: fixed;
    background-size: cover;
    color: #e0e0e0; /* 기본 텍스트 색상을 밝게 */
}

/* 헤더와 제목 색상 */
h1, h2, h3 {
    color: #ffffff;
}

/* 검색창 스타일 */
.stTextInput > div > div > input {
    background-color: rgba(255, 255, 255, 0.1);
    color: #ffffff;
    border-radius: 20px;
}

/* 확장(expander) 컴포넌트 스타일 */
.stExpander {
    background-color: rgba(255, 255, 255, 0.05);
    border-radius: 10px;
}
.stExpander header {
    color: #e0e0e0 !important;
}

/* 구분선 색상 */
hr {
    background-color: #444444;
}

/* 포스터 이미지 스타일 */
.stImage img {
    border-radius: 10px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    margin-bottom: 1rem;
}

</style>
""", unsafe_allow_html=True)


# --- 뮤지컬 데이터 (30개) ---
# 각 뮤지컬 정보에 포스터 URL을 추가합니다.
# 실제 이미지는 Base64로 인코딩하여 코드에 직접 포함합니다.
musicals_data = [
    {
        "title": "프랑켄슈타인",
        "poster_url": "http://googleusercontent.com/file_content/3",
        "summary": "19세기 유럽, 천재 과학자 빅터 프랑켄슈타인이 생명 창조에 성공하지만, 그가 만든 피조물에게 '괴물'이라는 이름으로 버림받으며 비극이 시작됩니다.",
        "cast": {
            "빅터 프랑켄슈타인": ["류정한", "유준상", "전동석", "민우혁", "규현"],
            "앙리 뒤프레/괴물": ["박은태", "한지상", "카이", "박민성", "정택운(레오)"],
            "엘렌": ["서지영", "박혜나", "안시하"],
            "줄리아": ["안시하", "이지혜", "박혜나"]
        }
    },
    {
        "title": "지킬앤하이드",
        "poster_url": "http://googleusercontent.com/file_content/5",
        "summary": "인간의 내면에 공존하는 선과 악을 분리하려는 의사 '지킬'이 실험을 통해 자신의 또 다른 인격인 '하이드'를 만들어내면서 벌어지는 비극적 스릴러입니다.",
        "cast": {
            "지킬/하이드": ["조승우", "류정한", "홍광호", "박은태", "전동석", "신성록", "박건형", "민우혁"],
            "루시": ["김선영", "옥주현", "아이비", "윤공주", "린아", "해나", "선민"],
            "엠마": ["조정은", "김소현", "임혜영", "이지혜", "최수진", "민경아"]
        }
    },
    {
        "title": "오페라의 유령",
        "poster_url": "http://googleusercontent.com/file_content/4",
        "summary": "파리 오페라 하우스 지하에 숨어 사는 천재 음악가 '유령'과 프리마돈나 '크리스틴', 그리고 귀족 '라울'의 비극적이고 아름다운 사랑 이야기입니다.",
        "cast": {
            "유령(팬텀)": ["윤영석", "홍광호", "박효신", "조승우", "최재림", "전동석"],
            "크리스틴": ["김소현", "이혜경", "임혜영", "손지수", "송은혜"],
            "라울": ["류정한", "정상윤", "송원근", "황건하"]
        }
    },
    {
        "title": "레미제라블",
        "poster_url": "http://googleusercontent.com/file_content/6",
        "summary": "빵 한 조각을 훔친 죄로 19년간 감옥살이를 한 장발장의 기구한 인생을 통해 인간의 존엄성과 사랑, 용서를 다룬 빅토르 위고 원작의 대서사시입니다.",
        "cast": {
            "장발장": ["정성화", "양준모", "민우혁", "최재림"],
            "자베르": ["문종원", "김우형", "카이", "김준현"],
            "판틴": ["조정은", "차지연", "린아"]
        }
    },
    {
        "title": "데스노트",
        "poster_url": "http://googleusercontent.com/file_content/7",
        "summary": "이름이 적히면 죽는 '데스노트'를 손에 넣은 천재 고등학생 라이토와 명탐정 엘(L)의 치열한 두뇌 싸움을 그린, 동명 만화 원작의 뮤지컬입니다.",
        "cast": {
            "야가미 라이토": ["홍광호", "고은성", "김성철"],
            "엘(L)": ["김준수", "김성철", "서경수"],
            "렘": ["박혜나", "김선영", "장은아"],
            "류크": ["강홍석", "서경수", "장지후"]
        }
    },
    {
        "title": "드라큘라",
        "poster_url": "http://googleusercontent.com/file_content/8",
        "summary": "수백 년 동안 한 여인만을 사랑해 온 드라큘라 백작의 이야기를 다룹니다. 거부할 수 없는 매력의 뱀파이어와 그를 둘러싼 인물들의 운명적인 사랑과 갈등을 그립니다.",
        "cast": {
            "드라큘라": ["김준수", "전동석", "신성록", "류정한"],
            "미나": ["조정은", "임혜영", "린아", "아이비", "박지연"],
            "반 헬싱": ["강태을", "손준호", "유준상"]
        }
    },
    {
        "title": "레베카",
        "poster_url": "http://googleusercontent.com/file_content/9",
        "summary": "죽은 전 부인 '레베카'의 그림자가 드리운 맨덜리 저택에 새로 들어온 '나(I)'가 집사 '댄버스 부인'과 맞서며 사랑과 자아를 찾아가는 미스터리 스릴러입니다.",
        "cast": {
            "막심 드 윈터": ["류정한", "민영기", "엄기준", "송창의", "카이", "신성록"],
            "댄버스 부인": ["옥주현", "신영숙", "차지연", "장은아", "리사"],
            "나(I)": ["임혜영", "김보경", "송상은", "루나", "이지혜", "박지연"]
        }
    },
    {
        "title": "엘리자벳",
        "poster_url": "http://googleusercontent.com/file_content/10",
        "summary": "오스트리아 황후 '엘리자벳'의 일대기에 '죽음(Der Tod)'이라는 판타지적 요소를 더해, 자유를 갈망했던 그녀의 삶을 드라마틱하게 그린 작품입니다.",
        "cast": {
            "엘리자벳": ["옥주현", "김소현", "신영숙", "이지혜", "김선영"],
            "죽음(토드)": ["김준수", "박효신", "전동석", "박형식", "정택운(레오)", "신성록"],
            "루케니": ["박은태", "이지훈", "강태을", "김수용"]
        }
    },
    {
        "title": "위키드",
        "poster_url": "http://googleusercontent.com/file_content/11",
        "summary": "도로시가 오즈에 오기 전, 초록 마녀 엘파바와 금발 마녀 글린다의 숨겨진 우정과 성장을 통해 선과 악의 편견을 깨는 감동적인 이야기입니다.",
        "cast": {
            "엘파바": ["옥주현", "박혜나", "차지연", "손승연"],
            "글린다": ["정선아", "김보경", "아이비", "나하나"],
            "피에로": ["민우혁", "고은성", "서경수", "진태화"]
        }
    },
    {
        "title": "헤드윅",
        "poster_url": "http://googleusercontent.com/file_content/12",
        "summary": "동독 출신의 트랜스젠더 록 가수 '헤드윅'이 자신의 실패한 사랑과 음악 인생에 대한 이야기를 콘서트 형식으로 풀어내는 모노드라마 뮤지컬입니다.",
        "cast": {
            "헤드윅": ["조승우", "오만석", "조정석", "유연석", "전동석", "마이클리", "정문성", "이규형", "렌"],
            "이츠학": ["전혜선", "이영미", "제이민", "유리아", "홍서영"]
        }
    },
    {
        "title": "영웅",
        "poster_url": "http://googleusercontent.com/file_content/13",
        "summary": "1909년, 하얼빈역에서 이토 히로부미를 저격한 안중근 의사의 마지막 1년을 그린 대한민국 대표 창작 뮤지컬입니다.",
        "cast": {
            "안중근": ["정성화", "양준모", "민우혁", "류정한", "신성록"],
            "이토 히로부미": ["김도형", "서영주", "이정열"],
            "설희": ["정재은", "린지", "리사"]
        }
    },
    {
        "title": "웃는 남자",
        "poster_url": "http://googleusercontent.com/file_content/14",
        "summary": "17세기 영국, 찢어진 입을 가진 기형적인 외모의 '그윈플렌'이 유랑극단에서 광대로 살아가며 겪는 사랑과 사회 부조리에 대한 이야기입니다.",
        "cast": {
            "그윈플렌": ["박효신", "박강현", "수호", "박은태", "규현"],
            "우르수스": ["정성화", "양준모", "민영기"],
            "데아": ["민경아", "이수빈", "양서윤"],
            "조시아나 여공작": ["신영숙", "옥주현", "김소향"]
        }
    },
    {
        "title": "노트르담 드 파리",
        "poster_url": "http://googleusercontent.com/file_content/15",
        "summary": "15세기 파리, 추악한 외모의 꼽추 종지기 '콰지모도'와 아름다운 집시 여인 '에스메랄다', 그리고 그녀를 둘러싼 세 남자의 비극적인 사랑과 숙명을 그린 작품입니다.",
        "cast": {
            "콰지모도": ["윤형렬", "홍광호", "케이윌", "정성화", "마이클리"],
            "에스메랄다": ["바다", "윤공주", "차지연", "전나영", "유리아"],
            "그랭구와르": ["박은태", "마이클리", "정동하", "이충주", "조휘"]
        }
    },
    {
        "title": "모차르트!",
        "poster_url": "http://googleusercontent.com/file_content/16",
        "summary": "천재 음악가 모차르트의 삶을 그리고 있지만, 그의 천재성을 상징하는 아이 '아마데'와의 갈등을 통해 자유를 갈망했던 인간 '볼프강'의 고뇌를 조명합니다.",
        "cast": {
            "볼프강 모차르트": ["박효신", "김준수", "박은태", "전동석", "규현", "수호", "김희재"],
            "콜로레도 대주교": ["민영기", "김준현", "손준호"],
            "콘스탄체 베버": ["정선아", "차지연", "김소향", "린아"]
        }
    },
    {
        "title": "시카고",
        "poster_url": "http://googleusercontent.com/file_content/17",
        "summary": "1920년대 재즈 시대의 시카고, 살인을 저지르고도 스타가 되길 꿈꾸는 '록시 하트'와 '벨마 켈리'의 이야기를 통해 당시 사회의 부조리와 허영을 풍자합니다.",
        "cast": {
            "벨마 켈리": ["최정원", "윤공주", "박칼린"],
            "록시 하트": ["아이비", "티파니 영", "민경아", "옥주현"],
            "빌리 플린": ["박건형", "최재림", "남경주"]
        }
    },
    {
        "title": "맘마미아!",
        "poster_url": "http://googleusercontent.com/file_content/18",
        "summary": "그리스의 작은 섬에서 엄마 '도나'와 사는 딸 '소피'가 자신의 결혼식을 앞두고 아빠일 가능성이 있는 세 남자를 초대하며 벌어지는 유쾌한 소동을 그립니다.",
        "cast": {
            "도나": ["최정원", "신영숙", "김선영"],
            "소피": ["박지연", "서현", "루나", "김금나"],
            "타냐": ["전수경", "김영주", "홍지민"]
        }
    },
    {
        "title": "킹키부츠",
        "poster_url": "http://googleusercontent.com/file_content/19",
        "summary": "폐업 위기에 처한 구두 공장을 물려받은 '찰리'가 드랙퀸 '롤라'를 만나 여장 남자를 위한 부츠 '킹키부츠'를 만들면서 벌어지는 신나는 이야기입니다.",
        "cast": {
            "롤라": ["정성화", "강홍석", "최재림", "박은태"],
            "찰리": ["이석훈", "김호영", "성규", "신재범"],
            "로렌": ["김지우", "김환희", "나하나"]
        }
    },
    {
        "title": "그날들",
        "poster_url": "http://googleusercontent.com/file_content/20",
        "summary": "故 김광석의 노래들로 이루어진 주크박스 뮤지컬. 청와대 경호실을 배경으로 20년 전 사라진 '그녀'와 경호원의 미스터리한 사건을 그립니다.",
        "cast": {
            "정학": ["유준상", "이건명", "최재웅", "오만석", "엄기준", "지창욱"],
            "무영": ["지창욱", "오종혁", "온주완", "양요섭", "규현", "남우현", "윤두준"],
            "그녀": ["김지현", "신다은", "루나", "방민아", "효정"]
        }
    },
    {
        "title": "서편제",
        "poster_url": "http://googleusercontent.com/file_content/21",
        "summary": "이청준의 동명 소설을 원작으로, 소리꾼 아버지 '유봉'과 그의 딸 '송화', 아들 '동호'의 한과 예술혼이 담긴 삶을 한국적인 정서와 음악으로 풀어낸 작품입니다.",
        "cast": {
            "송화": ["차지연", "이자람", "장은아", "이소연"],
            "동호": ["박영수", "김재범", "서범석"],
            "유봉": ["이정열", "서범석", "양준모"]
        }
    },
    {
        "title": "팬텀",
        "poster_url": "http://googleusercontent.com/file_content/22",
        "summary": "'오페라의 유령' 에릭의 인간적인 면모에 초점을 맞춰, 그의 비극적인 과거와 천재성, 그리고 크리스틴을 향한 순수한 사랑을 깊이 있게 다룬 작품입니다.",
        "cast": {
            "팬텀(에릭)": ["박효신", "박은태", "전동석", "카이", "규현", "류정한"],
            "크리스틴 다에": ["임선혜", "김소현", "이지혜", "김수"],
            "필립 드 샹동 백작": ["손준호", "박송권", "이해준"]
        }
    },
    {
        "title": "베르테르",
        "poster_url": "http://googleusercontent.com/file_content/23",
        "summary": "괴테의 소설 '젊은 베르테르의 슬픔'을 원작으로, '롯데'를 향한 '베르테르'의 순수하고도 열정적인 사랑과 그로 인한 깊은 고뇌를 서정적인 음악으로 풀어냅니다.",
        "cast": {
            "베르테르": ["조승우", "엄기준", "규현", "카이", "유연석", "나현우"],
            "롯데": ["이지혜", "김예원", "이지수"],
            "알베르트": ["이상현", "박은석", "김성철"]
        }
    },
    {
        "title": "스위니토드",
        "poster_url": "http://googleusercontent.com/file_content/25",
        "summary": "19세기 런던, 억울한 옥살이를 하고 돌아온 이발사 '벤자민 바커'가 '스위니 토드'로 이름을 바꾸고, 자신을 불행에 빠뜨린 자들에게 잔혹한 복수를 하는 이야기입니다.",
        "cast": {
            "스위니 토드": ["조승우", "류정한", "홍광호", "박은태", "강필석", "신성록"],
            "러빗 부인": ["옥주현", "전미도", "김지현", "린아", "이지혜"],
            "터핀 판사": ["김도형", "서영주", "박인배"]
        }
    },
    {
        "title": "팬레터",
        "poster_url": "http://googleusercontent.com/file_content/26",
        "summary": "1930년대 경성을 배경으로, 천재 소설가 '김해진'과 그를 동경하는 작가 지망생 '정세훈', 그리고 비밀에 싸인 천재 여류작가 '히카루'의 이야기를 다룬 미스터리 드라마입니다.",
        "cast": {
            "정세훈": ["문성일", "김성철", "려욱", "윤소호"],
            "김해진": ["김종구", "이규형", "김경수"],
            "히카루": ["소정화", "김히어라", "조지승"]
        }
    },
    {
        "title": "벤허",
        "poster_url": "http://googleusercontent.com/file_content/27",
        "summary": "귀족 가문의 자제였던 '유다 벤허'가 친구의 배신으로 노예로 전락한 후, 역경을 딛고 복수에 나서는 과정을 그린 장대한 스케일의 창작 뮤지컬입니다.",
        "cast": {
            "유다 벤허": ["유준상", "박은태", "카이", "신성록", "규현"],
            "메셀라": ["박민성", "이지훈", "서경수"],
            "에스더": ["윤공주", "아이비", "선민"]
        }
    },
    {
        "title": "빨래",
        "poster_url": "http://googleusercontent.com/file_content/28",
        "summary": "서울의 한 달동네를 배경으로, 서점에서 일하는 '나영'과 몽골 출신 이주노동자 '솔롱고'를 비롯한 서민들의 팍팍하지만 따뜻한 삶의 이야기를 그립니다.",
        "cast": {
            "서나영": ["홍지희", "강연정", "김주연"],
            "솔롱고": ["홍광호", "임창정", "이정은"],
            "주인 할매": ["이정은", "이미경"]
        }
    },
    # --- 5개 뮤지컬 추가 ---
    {
        "title": "마리 퀴리",
        "poster_url": "http://googleusercontent.com/file_content/29",
        "summary": "최초로 노벨상을 두 번 수상한 위대한 과학자 '마리 퀴리'의 삶을 다룹니다. 자신의 연구가 초래한 비극에 맞서며 진실을 찾아가는 그녀의 고뇌와 신념을 그립니다.",
        "cast": {
            "마리 퀴리": ["김소향", "옥주현", "리사"],
            "안느": ["김히어라", "이봄소리", "효정"],
            "피에르 퀴리": ["김찬호", "박영수", "임별"]
        }
    },
    {
        "title": "어쩌면 해피엔딩",
        "poster_url": "http://googleusercontent.com/file_content/30",
        "summary": "가까운 미래, 인간을 돕기 위해 만들어졌지만 구형이 되어 버려진 로봇 '올리버'와 '클레어'가 만나 사랑과 삶의 의미를 배워가는 따뜻하고 서정적인 이야기입니다.",
        "cast": {
            "올리버": ["정문성", "전성우", "신성민", "임준혁"],
            "클레어": ["전미도", "박지연", "강혜인", "한재아"]
        }
    },
    {
        "title": "호프",
        "poster_url": "http://googleusercontent.com/file_content/32",
        "summary": "현대 문학의 거장 요제프 클라인의 미발표 원고를 평생 지켜온 78세 노인 '에바 호프'의 삶을 통해, 원고가 곧 자신이었던 한 인간의 인생을 그립니다.",
        "cast": {
            "호프": ["김선영", "차지연", "김지현"],
            "K": ["고훈정", "조형균", "김경수"]
        }
    },
    {
        "title": "광화문 연가",
        "poster_url": "http://googleusercontent.com/file_content/31",
        "summary": "죽음을 앞둔 주인공 '명우'가 마지막 1분을 앞두고 '월하'와 함께 떠나는 시간 여행을 통해 자신의 젊은 날의 사랑과 우정을 되돌아보는 이야기입니다.",
        "cast": {
            "중년 명우": ["안재욱", "이건명", "강필석", "윤도현", "차지연"],
            "월하": ["구원영", "김호영", "이석훈", "정성화", "차지연"],
            "젊은 명우": ["허도영", "김성규", "박강현", "이찬동"]
        }
    },
    {
        "title": "사의 찬미",
        "poster_url": "http://googleusercontent.com/file_content/24",
        "summary": "1920년대 경성, 천재 극작가 김우진과 조선 최초의 소프라노 윤심덕의 비극적인 사랑과 실화를 바탕으로 한 뮤지컬입니다.",
        "cast": {
            "김우진": ["이해준", "김종구", "진태화"],
            "윤심덕": ["이지수", "최연우", "최수진"],
            "사내": ["최재웅", "김재범", "박정표"]
        }
    }
]


# --- 앱 UI 구성 ---

# 제목과 부제
st.title("🎭 한국 뮤지컬 대백과")
st.write("한국 뮤지컬의 모든 것을 한눈에! 제목과 배우 이름으로 검색해보세요.")

# 검색창
search_term = st.text_input("", placeholder="뮤지컬 제목 또는 배우 이름을 검색하세요...", label_visibility="collapsed")

# 검색 로직
filtered_musicals = []
if search_term:
    # 검색어가 있을 경우, 데이터 전체를 순회하며 필터링
    search_term_lower = search_term.lower()
    for musical in musicals_data:
        # 1. 뮤지컬 제목에 검색어가 포함되어 있는지 확인
        if search_term_lower in musical['title'].lower():
            filtered_musicals.append(musical)
            continue # 다음 뮤지컬로 넘어감

        # 2. 배우 이름에 검색어가 포함되어 있는지 확인
        found_in_cast = False
        for role, actors in musical['cast'].items():
            for actor in actors:
                if search_term_lower in actor.lower():
                    filtered_musicals.append(musical)
                    found_in_cast = True
                    break # 배우를 찾았으면 다음 역할로
            if found_in_cast:
                break # 역할을 찾았으면 다음 뮤지컬로
else:
    # 검색어가 없을 경우, 모든 뮤지컬을 보여줌
    filtered_musicals = musicals_data

# 결과 출력
if not filtered_musicals:
    st.warning(f"'{search_term}'에 대한 검색 결과가 없습니다.")
else:
    if search_term:
        st.info(f"총 {len(filtered_musicals)}개의 뮤지컬을 찾았습니다.")
    
    st.divider() # 구분선

    for musical in filtered_musicals:
        col1, col2 = st.columns([1, 2]) # 컬럼을 1:2 비율로 나눔
        
        with col1:
            st.image(musical['poster_url'], use_column_width=True)

        with col2:
            st.markdown(f"## <span style='color: #C0A062;'>{musical['title']}</span>", unsafe_allow_html=True)
            st.write(musical['summary'])

            # 출연진 정보는 확장 가능한 형태로 보여줌
            with st.expander("역대 주요 출연진 보기"):
                for role, actors in musical['cast'].items():
                    # st.markdown을 사용하여 굵은 글씨와 함께 배우 목록을 깔끔하게 표시
                    st.markdown(f"**{role}:** {', '.join(actors)}")
        
        st.divider() # 각 뮤지컬 정보 사이에 구분선 추가
