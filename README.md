# 日报可视化网站（公开仓库，只放网站本身）

本仓库只含公开网站静态页，不含老仓库的基建代码、不含密钥。

- index.html：近30天回购增持 + 当日涨停（中午版/下午版），直接读 Supabase 日报数据库，数据库更新后刷新即更新。
- 数据源：回购读 yjgj02gmail_buyback_track；涨停读 yjgj02gmail_limitup_daily（只展示最新交易日）。
- 部署：GitHub Pages，Source 选 Deploy from a branch，Branch 选 main，目录选根目录 /，网址为 https://yanjiugongju01.github.io/musegmail-daily-report-website/
- 涨停写库：报告生成后由游资技能步骤 7 的 0-token 脚本写入新表；建表 SQL 在老仓库 supabase/migrations/20261026_add_limitup_daily.sql，已在 Supabase 网页版执行。
