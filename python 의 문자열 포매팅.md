## python 의 문자열 포매팅

- % 연산자
- str.format
- f-string : 가장 간편하면서 강력한 방식입니다.(python 3.6+)

<br/>



## % 연산자

python 콘솔을 열고 아래의 코드를 작성해봅니다.<br/>



e.g.

```python
>>> world = "%s, world" %("Hello")
>>> print(world)
Hello, world
```

<br/>



integer 타입일 경우 아래와 같이 %i 로 읽어들입니다.

```python
>>> tomato = "%i won" %(1000)
>>> print(tomato)
1000 won
```

<br/>



이 경우 %i 로 지정해줬음에도 데이터의 타입이 일치하지 않으면 에러를 냅니다.

```python
>>> tomato = "%i won" %("1000")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %i format: a real number is required, not str
```

<br/>



문제점

- 아래와 같이 포매팅 문자열이 길어지면 알아보기도 힘들고 수정하기도 쉽지 않으며 데이터 타입 맞추기도 쉽지 않습니다.
- python3 공식문서에서는 `%` 포매팅을 권장하지 않는다고 이야기하고 있습니다. 개인적으로는 python 3.6 미만의 버전에서는 짧은 문자열은  `%` 포매팅을 사용하는게 그렇게 나쁘지는 않을 듯 합니다.

```python
>>> description = "%s %s? python 은 정말 강력한거 같아. 그렇지 않니 %s아? 그런데 요즘 한국 밥값이 한끼에 %i 원이라던데
사실이니? 맥도날드는 도대체 뭐하고 있는거니?" %("안녕", "세상", "세상놈", 10000)
>>> print(description)
```

<br/>



## str.format

간단한 사용법은 아래와 같습니다.

```python
>>> world = "{}, world".format("Hello")
>>> print(world)
Hello, world
```

<br/>



또는 순서를 지정하는 것이 가능합니다.

```python
>>> tomato = "{0} {1}".format(1000, "won")
>>> print(tomato)
1000 won
```

<br/>



dictionary 로 전달

- keyword argument 로 전달하는 것도 가능합니다.

```python
>>> tomato = "{price} {unit}".format(price=1000, unit="won")
>>> print(tomato)
1000 won
```

<br/>



문제점

- 문자열이 길어지면 복잡해지는 것은 여전합니다.

```python
>>> description = "{message} {target}? python 은 정말 강력한거 같아. 그렇지 않니 {hell}아? 그런데 요즘 한국 밥값이 한끼 에 {price}원이라던데 사실이니? 맥도날드는 도대체 뭐하고 있는거니?".format(message="안녕", target="세상", hell="세상놈", price=10000)
>>> print(description)
```

<br/>



## f-string

> f"문자열" 처럼 쌍따옴표로 감싸도 되고 f'문자열' 처럼 따옴표로 감싸도 됩니다.

가장 간편하면서 강력한 방식입니다.(python 3.6+)<br/>

간단하게 아래와 같은 형식으로 사용 가능합니다.

```bash
>>> world = f"{'Hello'}, world"
>>> print(world)
Hello, world
```

<br/>

또는 아래와 같이 변수를 지정하는 것 역시 가능합니다.

```python
>>> message = "Hello"
>>> world = f"{message}, world"
>>> print(world)
Hello, world
```

<br/>

`{}` 내에서 각종 연산을 수행하는 것 역시 가능합니다.

```python
>>> won = 30000
>>> usd_won = 1350
>>> target_price = f"{won/usd_won}"
>>> print(target_price)
22.22222222222222
```

<br/>



코틀린이나 Javascript 에서도 비슷한 문법이 있는데, python 에서도 3.6 버전부터 적용되었다는 것을 보면 친절한 언어 같다는 생각이 듭니다.<br/>

<br/>



## 성능 : `f-string` vs `str.format` vs `% 연산자`

직접 돌려봤는데, `% 연산자` 는 확실히 조금 느렸고, `f-string`, `str.format` 은 거의 비슷했습니다.<br/>

<br/>



`% 연산자` 테스트

```python
>>> timeit.timeit("""'a=%s b=%s c=%s d=%s e=%s' %(1,2,3,4,5)""", number=10000)
0.005094500025734305
```

<br/>



str.format 테스트

```python
>>> timeit.timeit("""'a={} b={} c={} d={} e={}'.format(1,2,3,4,5)""", number=10000)
0.0032825999660417438

>>> timeit.timeit("""'a={} b={} c={} d={} e={}'.format(1,2,3,4,5)""", number=10000)
0.006733100046403706
>>> timeit.timeit("""'a={} b={} c={} d={} e={}'.format(1,2,3,4,5)""", number=10000)
0.00678870000410825
>>> timeit.timeit("""'a={} b={} c={} d={} e={}'.format(1,2,3,4,5)""", number=10000)
0.006648399983532727
>>> timeit.timeit("""'a={} b={} c={} d={} e={}'.format(1,2,3,4,5)""", number=10000)
0.011466800002381206
>>> timeit.timeit("""'a={} b={} c={} d={} e={}'.format(1,2,3,4,5)""", number=10000)
0.006541399983689189
```

<br/>



`f-string` 테스트

```python
>>> timeit.timeit("""f'a={1} b={2} c={3} d={4} e={5}'""", number=10000)
0.006753399968147278
>>> timeit.timeit("""f'a={1} b={2} c={3} d={4} e={5}'""", number=10000)
0.00645540002733469
>>> timeit.timeit("""f'a={1} b={2} c={3} d={4} e={5}'""", number=10000)
0.0040822000009939075
>>> timeit.timeit("""f'a={1} b={2} c={3} d={4} e={5}'""", number=10000)
0.009278199984692037
>>> timeit.timeit("""f'a={1} b={2} c={3} d={4} e={5}'""", number=10000)
0.0031504000071436167
```

<br/>



