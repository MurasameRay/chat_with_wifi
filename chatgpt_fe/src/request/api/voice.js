import service from "..";

export const getVoiceURL = (word) => {
	return service({
		url: "chatWithWife/",
		method: "POST",
		data: {
			word: word,
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
