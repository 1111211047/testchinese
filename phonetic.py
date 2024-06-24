def read(expression):
    try:
        # 使用eval函数来计算表达式结果
        result = eval(expression)
        return(f"{expression} = {result}")
    except Exception as e:
        return(f"無法计算 '{expression}': {e}")

if __name__ == "__main__":
    while True:
        expression = input("请输入乘法表达式 (例如 1*1)，或輸入 'exit' 退出程序: ")
        
        if expression.lower() == 'exit':
            print("程序已退出。")
            break
        
