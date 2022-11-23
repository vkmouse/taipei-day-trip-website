import { AttractionState } from "./Core";

export interface API {
  getAttractions : (page: number, keyword: string) => Promise<AttractionState>
  getCategories: () => Promise<{ data: string[] }>
}

export let api : API = {
  getAttractions: () => new Promise(() => void 0),
  getCategories: () => new Promise(() => void 0),
};

export const setAPI = (newapi : API) => {
  api = newapi;
};
