
# nim c --app:lib libnimsample.nim
# nim c --out:libnimsample.so --app:lib libnimsample.nim

proc foo*(): void {.exportc, dynlib.} =
  echo "Hello, I am a shared library"

proc add*(a: int, b: int): int {.exportc, dynlib.} =
  return a + b

proc hello*(name: cstring): void {.exportc, dynlib.} =
  echo "Hello ", name
