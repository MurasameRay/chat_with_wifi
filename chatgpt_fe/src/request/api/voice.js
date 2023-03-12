import service from "..";

export const getVoice = (params) => {
	return service({
		url: `sayHi/?name=${params}`,
		method: "GET",
		// params: params,
	});
};
