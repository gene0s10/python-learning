def caesar(text, shift):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",]
    
    result = ""
    
    for char in text: 
        char_index = 0
        for i in range(26): 
            if char == alphabet[i]:
                char_index = i
        
        shifted_index = (char_index + shift) % 26 
        result += alphabet[shifted_index] 
        
    return result 


text = input("暗号化する文字列: ")
shift = int(input("ずらす文字数: "))

encrypted_text = caesar(text, shift)
print(f"暗号化結果: {encrypted_text}")











def caesar(text, shift):
    alphabet = [
        "あ", "い", "う", "え", "お", "か", "き", "く", "け", "こ", "さ", "し", "す",
        "せ", "そ", "た", "ち", "つ", "て", "と", "な", "に", "ぬ", "ね", "の", "は",
        "ひ", "ふ", "へ", "ほ", "ま", "み", "む", "め", "も","や", "ゆ", "よ","ら", "り",
        "る", "れ", "ろ","わ", "を", "ん"]
    
    result = ""
    
    for char in text: 
        char_index = 0
        for i in range(46): 
            if char == alphabet[i]:
                char_index = i
        
        shifted_index = (char_index + shift) % 46
        result += alphabet[shifted_index] 
        
    return result 


text = input("暗号化する文字列: ")
shift = int(input("ずらす文字数: "))

encrypted_text = caesar(text, shift)
print(f"暗号化結果: {encrypted_text}")