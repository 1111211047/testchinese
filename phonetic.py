def read(expression):
    try:
        # 使用eval函数来计算表达式结果
        result = eval(expression)
        return(f"{expression} = {result}")
    except Exception as e:
        return(f"無法计算 '{expression}': {e}")
