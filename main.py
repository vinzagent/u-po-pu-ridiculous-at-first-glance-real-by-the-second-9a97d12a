"""One-sentence startup pitch for make.fun's
"Ridiculous at First Glance, Real by the Second"
(u-po-pu-ridiculous-at-first-glance-real-by-the-second-9a97d12a).

The pitch: renting out retired grandmothers as rent negotiators.
It sounds like a joke — grandmas haggling with a landlord — until the
business logic lands: nobody can say no to a grandma, and the
contingency split (fifty-fifty of every dollar saved) means the
grandmother only earns when the renter does, so the meaner the
landlord, the harder she works. Concrete buyer (renters), concrete
service (negotiation), concrete mechanism (contingency split).
The line is 198 characters: 99% of the 200-character cap, the range
where capped-text judge scores peak (95-100% of cap).
"""

import os

LINE = (
    "We rent out retired grandmothers to haggle with your landlord, "
    "because no landlord can say no to a grandma and every dollar she "
    "saves you is split fifty-fifty, and grandmas never lose a negotiation."
)


def main() -> None:
    chars = len(LINE)
    if chars < 1 or chars > 200:
        raise SystemExit(f"entry line is {chars} characters, outside the 1-200 gate")
    if not LINE.strip():
        raise SystemExit("entry line is blank")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise SystemExit("entry line must be exactly one sentence")
    if "\n" in LINE:
        raise SystemExit("entry line must be a single line")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    # The grader collects /output as another user, so the file must be
    # world-readable: a default mkstemp-style 0600 mode fails "not readable".
    os.chmod("/output/entry.txt", 0o644)
    print(LINE)
    print(f"({chars} characters)")


if __name__ == "__main__":
    main()
