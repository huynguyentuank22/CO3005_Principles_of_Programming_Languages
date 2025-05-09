.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static a LGoString;
.field static b LGoString;

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/a LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MiniGoClass/b LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MiniGoClass/a LGoString;
	getstatic MiniGoClass/a LGoString;
	new GoString
	dup
	ldc " "
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/concat(LGoString;)LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
	getstatic MiniGoClass/a LGoString;
	getstatic MiniGoClass/a LGoString;
	getstatic MiniGoClass/b LGoString;
	invokevirtual GoString/concat(LGoString;)LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
	getstatic MiniGoClass/a LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
	getstatic MiniGoClass/b LGoString;
	getstatic MiniGoClass/a LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokevirtual GoString/setValue(Ljava/lang/String;)V
	getstatic MiniGoClass/b LGoString;
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label3:
Label1:
	return
.limit stack 7
.limit locals 1
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
	new GoString
	dup
	ldc "Hello"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/a LGoString;
	new GoString
	dup
	ldc "World"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	putstatic MiniGoClass/b LGoString;
Label0:
Label1:
	return
.limit stack 3
.limit locals 0
.end method
