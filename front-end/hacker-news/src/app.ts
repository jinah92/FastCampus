import Router from "./core/router";
import {NewsDetailView, NewsFeedView} from './page';
import {Store} from './types';

const store: Store = {
  currentPage: 1,
  feeds: [],
};

declare global {
  interface Window {
    store: Store;
  }
}

window.store = store; // 전역객체

// 웹 페이지에서 해시값(#) 변경될 떄 호출되는 함수
const router: Router = new Router();
const newsFeedView = new NewsFeedView('root');
const newsDetailView = new NewsDetailView('root');

router.setDefaultPage(newsFeedView);
router.addRouterPath('/page/', newsFeedView);
router.addRouterPath('/show/', newsDetailView);

router.route();