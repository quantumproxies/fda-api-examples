# FDA adverse events (openFDA) API — examples

Drug adverse-event reports from the FDA FAERS database — drugs, reactions, seriousness.

**Live page, full schema & pricing → [quanticdata.io/collectors/fda-api/](https://quanticdata.io/collectors/fda-api/)**

Reads the FDA's adverse-event reporting system via openFDA and delivers one row per report: seriousness and its reasons, the reported drugs, the reactions (MedDRA terms), patient sex and age, country, received date and report type. Search a drug name, or use openFDA's field:value query syntax. Keyless.

## Quick start (curl)

```bash
curl -X POST https://api.quanticdata.io/v1/scraper/collectors/openfda/run \
  -H "Authorization: Bearer $QD_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "ibuprofen", "max_results": 50}'
```

## Python

See [`example.py`](example.py):

```bash
export QD_API_KEY=qd_live_...   # https://quanticdata.io/
python3 example.py
```

## Inputs

- `query` (string, required) — A drug name, or an openFDA field:value query.
- `max_results` (integer) — How many reports to deliver at most (1–500). You pay only for delivered reports.

## Output — one row per report

| field | type | description |
|---|---|---|
| `rank` | integer | 1-based position. |
| `report_id` | string | FAERS safety report id. |
| `serious` | boolean | Whether the report is flagged serious. |
| `serious_reasons` | string[] | Death, hospitalization, life-threatening… |
| `drugs` | string[] | Reported medicinal products. |
| `reactions` | string[] | Reactions (MedDRA terms). |
| `patient_sex` | string | male/female when reported. |
| `patient_age` | string | Patient age as reported. |
| `country` | string | Country of occurrence. |
| `received_date` | string | Received date (ISO). |
| `report_type` | string | Report type code. |

## Pricing

**$0.0004 per delivered report** ($0.4 per 1,000). A run that delivers nothing costs nothing, and failed rows are never billed. The $2/month free allowance covers roughly 5,000 reports — no card required.

## Links

- This collector: https://quanticdata.io/collectors/fda-api/
- All collectors: https://quanticdata.io/collectors/
- Docs: https://quanticdata.io/docs/
