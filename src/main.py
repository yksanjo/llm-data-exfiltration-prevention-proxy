from datetime import datetime, timezone


def main() -> None:
    print("llm-data-exfiltration-prevention-proxy initialized at", datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    main()
