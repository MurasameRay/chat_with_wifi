import service from "..";

export const getVoice = (params) => {
	return service({
		url: "chatWithWife/",
		method: "POST",
		data: {
			word: params,
		},
	});
};

export const getRequest = (data) => {
	return service({
		url: `sayHi/?name=${data}`,
		method: "GET",
		// params: params,
	});
};
