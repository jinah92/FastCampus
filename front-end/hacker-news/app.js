const container = document.getElementById("root");
const ajax = new XMLHttpRequest(); //네트워크를 통해 데이터를 가져오는 도구 (반환값을 ajax 변수에 저장)
const content = document.createElement("div");
const NEWS_ULR = "https://api.hnpwa.com/v0/news/1.json";
const CONTENT_URL = "https://api.hnpwa.com/v0/item/@id.json";

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
  for (let i = 0; i < 10; i++) {
    newsList.push(`
    <li>
        <a href="#${newsFeed[i].id}">${newsFeed[i].title}(${newsFeed[i].comments_count})</a>
    </li>
  `);
  }

  newsList.push("</ul>");

  container.innerHTML = newsList.join("");
}

function newsDetail() {
  const id = location.hash.substr(1); // 선택한 콘텐츠의 id부분만을 추출

  const newsContent = getData(CONTENT_URL.replace("@id", id)); // 해당 콘텐츠 정보 요청 & 응답받은 콘텐츠를 JAON 파싱하여 저장

  container.innerHTML = `
    <h1>${newsContent.title}</h1>
    <div>
    <a href="#">목록으로</a>
    </div>
  `;
}

function router() {
  const routePath = location.hash;

  if (routePath === "") {
    //첫 진입
    newsFeed();
  } else {
    newsDetail();
  }
}

// 웹 페이지에서 해시값(#) 변경될 떄 호출되는 함수
window.addEventListener("hashchange", router);
router();
