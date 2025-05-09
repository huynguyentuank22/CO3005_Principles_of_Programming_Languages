.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object

.method public static test()LGoString;
Label0:
Label2:
.var 0 is a LGoString; from Label2 to Label3
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	astore_0
.var 1 is b LGoString; from Label2 to Label3
	new GoString
	dup
	ldc "World"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	astore_1
.var 2 is c LGoString; from Label2 to Label3
	aload_0
	aload_1
	invokevirtual GoString/concat(LGoString;)LGoString;
	astore_2
	aload_2
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 3
.end method

.method public static test1()LGoString;
Label0:
Label2:
	new GoString
	dup
	ldc "vibe coding"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	areturn
Label3:
Label1:
.limit stack 3
.limit locals 0
.end method

.method public static foo(LGoString;)V
.var 0 is s LGoString; from Label0 to Label1
Label0:
Label2:
	aload_0
	aload_0
	new GoString
	dup
	ldc "lala"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/concat(LGoString;)LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
	aload_0
	aload_0
	new GoString
	dup
	ldc "meowmeow"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/concat(LGoString;)LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 8
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is str1 LGoString; from Label2 to Label3
	invokestatic MiniGoClass/test()LGoString;
	astore_1
	aload_1
	invokestatic MiniGoClass/foo(LGoString;)V
	aload_1
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
.var 2 is str2 LGoString; from Label2 to Label3
	invokestatic MiniGoClass/test1()LGoString;
	astore_2
	aload_2
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
	aload_2
	invokestatic MiniGoClass/foo(LGoString;)V
	aload_2
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 1
.limit locals 3
.end method

.method public <init>()V
.var 0 is this LMiniGoClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label4:
Label5:
Label1:
	return
.limit stack 1
.limit locals 1
.end method

.method public static <clinit>()V
Label0:
Label1:
	return
.limit stack 0
.limit locals 0
.end method
