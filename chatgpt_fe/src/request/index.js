import axios from "axios";

let service = axios.create({
	baseURL: "http://localhost:8000/api/",
	timeout: 100000,
});

// 请求拦截处理 请求拦截 在请求拦截中可以补充请求相关的配置
// interceptors axios的拦截器对象
service.interceptors.request.use(
	(config) => {
		// config 请求的所有信息
		// console.log(config);
		// 响应成功的返回
		return config; // 将配置完成的config对象返回出去 如果不返回 请求讲不会进行
	},
	(err) => {
		// 请求发生错误时的相关处理 抛出错误
		//  //响应失败的返回
		Promise.reject(err);
	}
);

//响应拦截处理  响应拦截器：包含两个函数（一个是成功返回的函数，一个是失败的返回的函数）
service.interceptors.response.use(
	(res) => {
		// 我们一般在这里处理，请求成功后的错误状态码 例如状态码是500，404，403
		// res 是所有相应的信息
		console.log(res);
		return res.data;
	},
	(err) => {
		// 服务器响应发生错误时的处理
		Promise.reject(err);
	}
);

export default service;
