import service from "..";

export const getVoice = (params) => {
	return service({
		url: "/api/sayHi/",
		method: "post",
		data: params,
	});
};
