# 日报可视化网站（公开仓库，只放网站本身）

本仓库只含公开网站静态页，不含老仓库的基建代码、不含密钥。

- index.html：近30天回购增持 + 当日涨停（中午版/下午版），只读本站同源 data.json（不直连数据库接口，避免浏览器跨域被挡）。
- data.json：由 .github/workflows/update-data.yml 定时从日报数据库公开网关同步生成（周一至周五北京时间约 12:05、16:35、18:05，对应中午版、下午版、回购日报之后），也可用 workflow_dispatch 手动触发；本地生成脚本为 dump_data.py（标准库 + curl 方式的公开网关读接口，无密钥）。
- 数据源：回购读 yjgj02gmail_buyback_track；涨停读 yjgj02gmail_limitup_daily（只展示最新交易日）。
- 部署：GitHub Pages，Source 选 Deploy from a branch，Branch 选 main，目录选根目录 /，网址为 https://yanjiugongju01.github.io/musegmail-daily-report-website/
- 涨停写库：报告生成后由游资技能步骤 7 的 0-token 脚本写入新表；建表 SQL 在老仓库 supabase/migrations/20261026_add_limitup_daily.sql，已在 Supabase 网页版执行。
