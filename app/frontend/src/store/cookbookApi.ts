import { api } from "./api";
const injectedRtkApi = api.injectEndpoints({
  endpoints: (build) => ({
    getRecipesRecipesGet: build.query<
      GetRecipesRecipesGetApiResponse,
      GetRecipesRecipesGetApiArg
    >({
      query: () => ({ url: `/recipes/` }),
    }),
    getRecipesByIdRecipesRecipeIdGet: build.query<
      GetRecipesByIdRecipesRecipeIdGetApiResponse,
      GetRecipesByIdRecipesRecipeIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/recipes/${queryArg.recipeId}` }),
    }),
    getUsersUsersGet: build.query<
      GetUsersUsersGetApiResponse,
      GetUsersUsersGetApiArg
    >({
      query: () => ({ url: `/users/` }),
    }),
    getUserByIdUsersUserIdGet: build.query<
      GetUserByIdUsersUserIdGetApiResponse,
      GetUserByIdUsersUserIdGetApiArg
    >({
      query: (queryArg) => ({ url: `/users/${queryArg.userId}` }),
    }),
    getSecureUsersSecureGet: build.query<
      GetSecureUsersSecureGetApiResponse,
      GetSecureUsersSecureGetApiArg
    >({
      query: () => ({ url: `/users/secure` }),
    }),
  }),
  overrideExisting: false,
});
export { injectedRtkApi as cookbookApi };
export type GetRecipesRecipesGetApiResponse =
  /** status 200 Successful Response */ Recipe[];
export type GetRecipesRecipesGetApiArg = void;
export type GetRecipesByIdRecipesRecipeIdGetApiResponse =
  /** status 200 Successful Response */ Recipe;
export type GetRecipesByIdRecipesRecipeIdGetApiArg = {
  recipeId: number;
};
export type GetUsersUsersGetApiResponse =
  /** status 200 Successful Response */ User[];
export type GetUsersUsersGetApiArg = void;
export type GetUserByIdUsersUserIdGetApiResponse =
  /** status 200 Successful Response */ User;
export type GetUserByIdUsersUserIdGetApiArg = {
  userId: number;
};
export type GetSecureUsersSecureGetApiResponse =
  /** status 200 Successful Response */ string;
export type GetSecureUsersSecureGetApiArg = void;
export type Owner = {
  id: number;
  profile_picture: string;
  english_name: string;
  recipes: number[];
  description: string;
};
export type RecipeAdditionalInformation = {
  prep_time: number;
  work_time: number;
  servings: number;
};
export type ScaleOption = "g" | "K" | "cup" | "aunce" | "teaspoon" | "spoon";
export type NutritionValue = {
  name: string;
  scale?: ScaleOption;
  value: number;
};
export type Ingredient = {
  name: string;
  scale?: ScaleOption;
  value?: number;
};
export type SimpleStep = {
  title: string;
  description?: string;
  pictures_url?: string[];
};
export type TimeStep = {
  title: string;
  description?: string;
  pictures_url?: string[];
  timer?: number;
};
export type Recipe = {
  title: string;
  description?: string;
  pictures_url?: string[];
  id: number;
  owner: Owner;
  tags?: string[];
  additional_info: RecipeAdditionalInformation;
  nutrition?: NutritionValue[];
  equipment?: string[];
  ingredients: Ingredient[];
  sections: (SimpleStep | TimeStep)[];
};
export type ValidationError = {
  loc: (string | number)[];
  msg: string;
  type: string;
};
export type HttpValidationError = {
  detail?: ValidationError[];
};
export type User = {
  id: number;
  profile_picture: string;
  english_name: string;
  recipes: number[];
};
export const {
  useGetRecipesRecipesGetQuery,
  useGetRecipesByIdRecipesRecipeIdGetQuery,
  useGetUsersUsersGetQuery,
  useGetUserByIdUsersUserIdGetQuery,
  useGetSecureUsersSecureGetQuery,
} = injectedRtkApi;
