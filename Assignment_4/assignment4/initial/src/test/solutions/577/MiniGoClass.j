.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static counter I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
	iconst_0
	dup
	ifle Label6
	pop
	invokestatic MiniGoClass/incrementAndGet()I
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
Label6:
	dup
	ifle Label9
	pop
	invokestatic MiniGoClass/incrementAndGet()I
	iconst_0
	if_icmple Label7
	iconst_1
	goto Label8
Label7:
	iconst_0
Label8:
Label9:
	ifle Label10
Label12:
Label13:
	new GoString
	dup
	ldc "This won't print"
	invokespecial GoString/<init>(Ljava/lang/String;)V
	invokevirtual GoString/getValue()Ljava/lang/String;
	invokestatic io/putStringLn(Ljava/lang/String;)V
Label14:
Label10:
Label11:
	getstatic MiniGoClass/counter I
	invokestatic io/putIntLn(I)V
	iconst_0
	putstatic MiniGoClass/counter I
	iconst_1
	dup
	ifgt Label17
	pop
	invokestatic MiniGoClass/incrementAndGet()I
	iconst_0
	if_icmple Label15
	iconst_1
	goto Label16
Label15:
	iconst_0
Label16:
Label17:
	dup
	ifgt Label20
	pop
	invokestatic MiniGoClass/incrementAndGet()I
	iconst_0
	if_icmple Label18
	iconst_1
	goto Label19
Label18:
	iconst_0
Label19:
Label20:
	ifle Label21
Label23:
Label24:
	getstatic MiniGoClass/counter I
	invokestatic io/putIntLn(I)V
Label25:
Label21:
Label22:
Label3:
Label1:
	return
.limit stack 17
.limit locals 1
.end method

.method public static incrementAndGet()I
Label0:
Label2:
	getstatic MiniGoClass/counter I
	iconst_1
	iadd
	putstatic MiniGoClass/counter I
	getstatic MiniGoClass/counter I
	ireturn
Label3:
Label1:
.limit stack 3
.limit locals 0
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
	iconst_0
	putstatic MiniGoClass/counter I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
