"""Dump buyback + limitup rows from the public Feishu gateway into data.json (0-token, stdlib only)."""
import json, urllib.parse, urllib.request
from datetime import date, datetime, timedelta, timezone

BASE = "https://jioclrmrlknmvszkkhph.supabase.co/functions/v1/yjgj02gmail-feishu-test"
BJ = timezone(timedelta(hours=8))

def fetch(table, select, gte):
    q = urllib.parse.urlencode({"action": "db_read", "table": table, "select": select, "limit": "1000", "report_date": f"gte.{gte}"})
    with urllib.request.urlopen(BASE + "?" + q, timeout=60) as r:
        return json.load(r).get("rows", [])

def main():
    today = datetime.now(BJ).date()
    bb = fetch("yjgj02gmail_buyback_track",
               "report_date,market,code,name,event_label,event_type,amount_yuan,market_cap_yuan,buyback_ratio,method,purpose,stage,score,admitted,guru_tag",
               (today - timedelta(days=30)).isoformat())
    lu = fetch("yjgj02gmail_limitup_daily",
               "report_date,version,code,name,pct,boards,board_count,zt_time,volume_wan,turnover_pct,market_cap_yi,float_cap_yi,industry,logic,grade,strength,disclosure_date",
               (today - timedelta(days=7)).isoformat())
    # Source tables can contain exact duplicate rows (gateway is insert-only);
    # dedupe on display so the site does not show the same row twice.
    def dedupe(rows):
        seen, out = set(), []
        for r in rows:
            k = json.dumps(r, sort_keys=True, ensure_ascii=False)
            if k not in seen:
                seen.add(k); out.append(r)
        return out
    bb, lu = dedupe(bb), dedupe(lu)
    out = {"generated_at_beijing": datetime.now(BJ).strftime("%Y-%m-%d %H:%M"),
           "buyback": bb, "limitup": lu}
    with open("data.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False)
    print(f"buyback={len(bb)} limitup={len(lu)} generated_at={out['generated_at_beijing']}")

if __name__ == "__main__":
    main()
