const ajax = new XMLHttpRequest(); //네트워크를 통해 데이터를 가져오는 도구 (반환값을 ajax 변수에 저장)
const NEWS_ULR = "https://api.hnpwa.com/v0/news/1.json";

ajax.open("GET", NEWS_ULR, false); //동기적 GET요청
ajax.send();

const newsFeed = JSON.parse(ajax.response); // JSON 형태로 응답값을 변환
console.log(newsFeed); // 응답값을 콘솔창에서 확인

const ul = document.createElement("ul");

// 반복문을 통한 데이터 표현
for (let i = 0; i < 10; i++) {
  const li = document.createElement("li");
  li.innerHTML = newsFeed[i].title;

  ul.appendChild(li);
}

document.getElementById("root").appendChild(ul);
