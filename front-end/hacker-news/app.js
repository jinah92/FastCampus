const container = document.getElementById("root");
const ajax = new XMLHttpRequest(); //네트워크를 통해 데이터를 가져오는 도구 (반환값을 ajax 변수에 저장)
const content = document.createElement("div");
const NEWS_ULR = "https://api.hnpwa.com/v0/news/1.json";
const CONTENT_URL = "https://api.hnpwa.com/v0/item/@id.json";

ajax.open("GET", NEWS_ULR, false); //동기적 GET요청
ajax.send();

const newsFeed = JSON.parse(ajax.response); // JSON 형태로 응답값을 변환
console.log(newsFeed); // 응답값을 콘솔창에서 확인

const ul = document.createElement("ul");

// 웹 페이지에서 해시값(#) 변경될 떄 호출되는 함수
window.addEventListener("hashchange", function () {
  const id = this.location.hash.substr(1); // 선택한 콘텐츠의 id부분만을 추출
  ajax.open("GET", CONTENT_URL.replace("@id", id), false); // 해당 콘텐츠 정보 요청
  ajax.send();

  const newsContent = JSON.parse(ajax.response); // 응답받은 콘텐츠를 JAON 파싱하여 저장
  const title = this.document.createElement("h1");

  title.innerHTML = newsContent.title;

  content.appendChild(title);
  console.log(newsContent);
});

// 반복문을 통한 데이터 표현
for (let i = 0; i < 10; i++) {
  const li = document.createElement("li");
  const a = document.createElement("a"); // 엥커 태그로 감싸기

  a.href = `#${newsFeed[i].id}`; // 링크 속성 추가
  a.innerHTML = `${newsFeed[i].title}(${newsFeed[i].comments_count})`;

  li.appendChild(a);
  ul.appendChild(li);
}

container.appendChild(ul);
container.appendChild(content);
