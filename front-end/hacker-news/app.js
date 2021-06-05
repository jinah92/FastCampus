const container = document.getElementById("root");
const ajax = new XMLHttpRequest(); //네트워크를 통해 데이터를 가져오는 도구 (반환값을 ajax 변수에 저장)
const content = document.createElement("div");
const NEWS_ULR = "https://api.hnpwa.com/v0/news/1.json";
const CONTENT_URL = "https://api.hnpwa.com/v0/item/@id.json";
const store = {
  currentPage: 1,
};

// API 요청 함수
function getData(url) {
  ajax.open("GET", url, false);
  ajax.send();

  return JSON.parse(ajax.response);
}

function newsFeed() {
  const newsFeed = getData(NEWS_ULR); // JSON 형태로 응답값을 변환
  const newsList = []; //배열을 이용하여, DOM API를 대체

  newsList.push("<ul>");
  // 반복문을 통한 데이터 표현
  for (let i = (store.currentPage - 1) * 10; i < store.currentPage * 10; i++) {
    newsList.push(`
    <li>
        <a href="#/show/${newsFeed[i].id}">${newsFeed[i].title}(${newsFeed[i].comments_count})</a>
    </li>
  `);
  }

  newsList.push("</ul>");
  newsList.push(`
    <div>
        <a href="#/page/${store.currentPage > 1 ? store.currentPage - 1 : 1}">이전 페이지</a>
        <a href="#/page/${store.currentPage + 1}">다음 페이지</a>
    </div>
  `);

  container.innerHTML = newsList.join("");
}

function newsDetail() {
  const id = location.hash.substr(7); // 선택한 콘텐츠의 id부분만을 추출

  const newsContent = getData(CONTENT_URL.replace("@id", id)); // 해당 콘텐츠 정보 요청 & 응답받은 콘텐츠를 JAON 파싱하여 저장

  container.innerHTML = `
    <h1>${newsContent.title}</h1>
    <div>
    <a href="#/page/${store.currentPage}">목록으로</a>
    </div>
  `;
}

function router() {
  const routePath = location.hash;

  if (routePath === "") {
    // 첫 진입
    newsFeed();
  } else if (routePath.indexOf("#/page/") >= 0) {
    // 페이지 목록화면
    store.currentPage = Number(routePath.substr(7));
    newsFeed();
  } else {
    // 콘텐츠 상세화면
    newsDetail();
  }
}

// 웹 페이지에서 해시값(#) 변경될 떄 호출되는 함수
window.addEventListener("hashchange", router);
router();
