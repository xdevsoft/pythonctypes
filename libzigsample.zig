const std = @import("std");

export fn foo() void {
  std.debug.print("Hello, world!\n", .{});
}

export fn add(a: i32, b: i32) i32 {
  return a + b;
}

export fn hello(name: [*:0]const u8) void {
  std.debug.print("Hello, {s}\n", .{name});
}

//zig build-lib -dynamic libzigsample.zig -femit-bin=libzigsample.so
