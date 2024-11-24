class Circle():
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def print_hi(self):
        # Use a breakpoint in the code line below to debug your script.
        print(f'Hi, {self.name}')  # Press Ctrl+F8 to toggle the breakpoint.

    def rmb_number_convert(self):
        # 12889.334
        # 壹万零肆佰伍拾元|伍角捌分

        result = ""
        # 函数参数,tuples,()
        # 字符串操作,字典,json{},
        # 壹万零肆佰伍拾元|伍角捌分
        rmb_dict = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
        low_rmb = ["", "拾", "佰", "仟"]
        high_rmb = ["", "万", "亿", "兆"]
        s_rmb = ["角", "分"]
        rmb_suffix = "元"
        str_number = f"{self.number:.2f}"
        print(str_number)
        int_part, float_part = str_number.split(".")
        print(int_part, float_part)
        if int(int_part) > 0:
            int_part_length = len(int_part)
            zero_flag = False
            for i, c_part in enumerate(int_part):
                real_number = int(c_part)
                low_index = (int_part_length - 1 - i) % 4
                high_index = (int_part_length - 1 - i) // 4
                # print(low_index,high_index)
                if real_number != 0:
                    if zero_flag:
                        result += rmb_dict[0]
                    result += rmb_dict[real_number] + low_rmb[low_index]
                    zero_flag = False
                else:
                    zero_flag = True
                if low_index % 4 == 0:
                    result += high_rmb[high_index]
                # print(i,c_part)
            result += rmb_suffix
        else:
            # result = result + ""
            result += rmb_dict[0] + rmb_suffix

        if int(float_part) > 0:
            for i, c_part in enumerate(float_part):
                real_number = int(c_part)
                result += rmb_dict[real_number] + s_rmb[i]
        else:
            result += "整"
        print(result)


def test():
    print("=######################################===========")