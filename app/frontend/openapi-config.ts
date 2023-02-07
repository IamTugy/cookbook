import type { ConfigFile } from '@rtk-query/codegen-openapi'

const config: ConfigFile = {
  schemaFile: 'http://localhost:8443/api/v1/openapi.json',
  apiFile: './src/store/api.ts',
  apiImport: 'api',
  outputFile: './src/store/cookbookApi.ts',
  exportName: 'cookbookApi',
  hooks: true,
}

export default config
