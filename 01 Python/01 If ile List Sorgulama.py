"""
Bu kodun amacı bir list içinde gönderilen değerin var olup olmamasına göre işlem yaptırmak.

if a in list 

şeklinde bir kullanımı mevcuttur. 

a ile gönderilen değer list içinde tek tek karşılaştırılır. Eğer eşleşme olmazsa geriye False döner. Bir noktada bir eşleşme gerçekleşirse araştırma bulduğu adımda durur ve geriye True değeri döner.
"""

requestMethodList = ["POST", "GET", "DELETE"]

method = input("Method'u giriniz: ")

if method in requestMethodList:
    print("Başarılı")
else:
    print("Tanımlı Olmayan Method")