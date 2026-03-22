from compute_risk import compute_risk
from app import Customer
import json
import sys

def risk_test():
    with open("test.json", 'r') as f:
        test_data = json.load(f)

    out = {}
    count = 0

    for index, test in enumerate(test_data):
        customer = Customer(**test['data'])
        res = compute_risk(customer)

        if test["expected"] == res:
            out[f"TestCase{index+1}"] = "Passed"
            count += 1
        else:
            out[f"TestCase{index+1}"] = "Failed"

    with open("result.json", "w") as f:
        json.dump(out, f, indent=2)

    print("\nTest Results:")
    print(json.dumps(out, indent=2))

    return count == len(test_data)


if __name__ == "__main__":
    success = risk_test()

    if not success:
        print("\n❌ Some tests FAILED")
        sys.exit(1)
    else:
        print("\n✅ All tests PASSED")
        sys.exit(0)