const container = document.getElementById("root");
const ajax = new XMLHttpRequest(); //네트워크를 통해 데이터를 가져오는 도구 (반환값을 ajax 변수에 저장)
const content = document.createElement("div");
const NEWS_ULR = "https://api.hnpwa.com/v0/news/1.json";
const CONTENT_URL = "https://api.hnpwa.com/v0/item/@id.json";
const store = {
  currentPage: 1,
  feeds: [],
};

// API 요청 함수
function getData(url) {
  ajax.open("GET", url, false);
  ajax.send();

  return JSON.parse(ajax.response);
}

function makeFeeds(feeds) {
  // 읽은 뉴스 피드 상태 관리
  for (let i = 0; i < feeds.length; i++) {
    feeds[i].read = false;
  }

  return feeds;
}

function newsFeed() {
  let newsFeed = store.feeds; // JSON 형태로 응답값을 변환
  const newsList = []; //배열을 이용하여, DOM API를 대체
  let template = `
    <div class="bg-gray-600 min-h-screen">
    <div class="bg-white text-xl">
     <div class="mx-auto px-4">
      <div class="flex justify-between items-center py-6">
       <div class="flex justify-start">
         <h1 class="font-extrabold">Hacker News</h1>
       </div>
       <div class="items-center justify-end">
        <a href="#/page/{{__prev_page__}}" class="text-gray-500">Previous</a>
        <a href="#/page/{{__next_page__}}" class="text-gray-500 ml-4">Next</a>
       </div>
      </div>
     </div>
    </div>
    <div class="p-4 text-2xl text-gray-700">
        {{__news_feed__}}
    </div>
    </div>
  `;

  if (newsFeed.length === 0) {
    // 최초 진입 시 api를 통해 가져오기
    newsFeed = store.feeds = makeFeeds(getData(NEWS_ULR));
  }

  // 반복문을 통한 데이터 표현
  for (let i = (store.currentPage - 1) * 10; i < store.currentPage * 10; i++) {
    newsList.push(`
    <div class="p-6 ${
      newsFeed[i].read ? "bg-red-500" : "bg-white"
    } mt-6 rounded-lg shadow-md transition-colors duration-500 hover:bg-green-100">
    <div class="flex">
     <div class="flex-auto">
      <a href="#/show/${newsFeed[i].id}">${newsFeed[i].title}</a>
     </div>
     <div class="text-center text-sm">
        <div class="w-10 text-white bg-green-300 rounded-lg px-0 py-2">${
          newsFeed[i].comments_count
        }</div>
     </div>
    </div>
    <div class="flex mt-3">
     <div class="grid grid-cols-3 text-sm text-gray-500">
        <div><i class="fas fa-user mr-1"></i>${newsFeed[i].user}</div>
        <div><i class="fas fa-heart mr-1"></i>${newsFeed[i].points}</div>
        <div><i class="fas fa-clock mr-1"></i>${newsFeed[i].time_ago}</div>
     </div>
    </div>
    </div>
  `);
  }

  template = template.replace("{{__news_feed__}}", newsList.join(""));
  template = template.replace(
    "{{__prev_page__}}",
    store.currentPage > 1 ? store.currentPage - 1 : 1
  );
  template = template.replace("{{__next_page__}}", store.currentPage + 1);

  container.innerHTML = template;
}

function newsDetail() {
  const id = location.hash.substr(7); // 선택한 콘텐츠의 id부분만을 추출
  const newsContent = getData(CONTENT_URL.replace("@id", id)); // 해당 콘텐츠 정보 요청 & 응답받은 콘텐츠를 JAON 파싱하여 저장

  let template = `
    <div class="bg-gray-600 min-h-screen pb-8">
    <div class="bg-white text-xl">
        <div class="mx-auto px-4">
            <div class="flex justify-between items-center py-6">
                <div class="flex justify-start">
                    <h1 class="font-extrabold">Hacker News</h1>
                </div>
                <div class="items-center justify-end">
                    <a href="#/page/${store.currentPage}" class="text-gray-500">
                        <i class="fa fa-times"></i>
                    </a>
                </div>
            </div>
        </div>
    </div>

    <div class="h-full border rounded-xl bg-white m-6 p-4">
     <h2>${newsContent.title}</h2>
     <div class="text-gray-400 h-20">
        ${newsContent.content}
     </div>

     {{__comments__}}
    </div>
  `;

  // 읽은 피드에 대한 상태 변경 (붉은색)
  for (let i = 0; i < store.feeds.length; i++) {
    if (store.feeds[i].id === Number(id)) {
      store.feeds[i].read = true;
      break;
    }
  }

  function makeComment(comments, called = 0) {
    const commentString = [];

    for (let i = 0; i < comments.length; i++) {
      commentString.push(`
        <div style="padding-left: ${called * 40}px;" class="mt-4">
         <div class="text-gray-400">
          <i class="fa fa-sort-up mr-2"></i>
          <strong>${comments[i].user}</strong> ${comments[i].time_ago}
         </div>
         <p class="text-gray-700">${comments[i].content}</p>
        </div>      
    `);

      if (comments[i].comments.length > 0) {
        commentString.push(makeComment(comments[i].comments, called + 1));
      }
    }

    return commentString.join("");
  }

  container.innerHTML = template.replace("{{__comments__}}", makeComment(newsContent.comments));
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