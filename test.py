## 電卓を作りたい

## 1. 2つの数値を入力する
def input_num():
    num1 = int(input("1つ目の数値を入力してください: "))
    num2 = int(input("2つ目の数値を入力してください: "))
    return num1, num2
## 2. 1つの演算子を入力する
def input_operator():
    operator = input("演算子を入力してください: ")
    return operator

## 3. 1と2の結果を出力する
def output(num1, num2, operator):
    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "*":
        print(num1 * num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "%":
        print(num1 % num2)
    elif operator == "**":
        print(num1 ** num2)
    else:
        print("演算子が間違っています")

## 4. 続けるか確認してから1と2を繰り返す
def main():
    while True:
        num1, num2 = input_num()
        operator = input_operator()
        output(num1, num2, operator)
        print("続けますか？")
        if input("y/n: ") == "n":
            break

if __name__ == "__main__":
    main()
