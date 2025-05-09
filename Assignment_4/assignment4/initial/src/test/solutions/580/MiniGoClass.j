.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static arrStr(LGoString;)[LGoString;
.var 0 is v LGoString; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/MAX I
	anewarray GoString
	dup
	iconst_0
	new GoString
	dup
	ldc "abc"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	dup
	iconst_1
	new GoString
	dup
	ldc "xyz"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	areturn
Label3:
Label1:
.limit stack 7
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is a [LGoString; from Label2 to Label3
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokestatic MiniGoClass/arrStr(LGoString;)[LGoString;
	astore_1
	aload_1
	iconst_0
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
.var 2 is b LGoString; from Label2 to Label3
	aload_1
	iconst_0
	aaload
	astore_2
	aload_1
	iconst_0
	new GoString
	dup
	ldc "def"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	aastore
	aload_2
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_0
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	aload_1
	iconst_1
	aaload
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 8
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
	iconst_2
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
