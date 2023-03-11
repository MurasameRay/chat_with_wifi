import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
const defaultChat = () => import("../components/dialog/defaultDialog.vue");
const newChat1 = () => import("../components/dialog/newDialogOne.vue");
const routes = [
	{
		path: "/",
		name: HomeView,
		component: HomeView,
		children: [
			{
				// 当 /user/:id/profile 匹配成功
				// UserProfile 将被渲染到 User 的 <router-view> 内部
				path: "defaultChat",
				component: defaultChat,
			},
			{
				// 当 /user/:id/posts 匹配成功
				// UserPosts 将被渲染到 User 的 <router-view> 内部
				path: "newChat1",
				component: newChat1,
			},
		],
	},
];

const router = createRouter({
	history: createWebHistory(),
	routes,
});

export default router;
