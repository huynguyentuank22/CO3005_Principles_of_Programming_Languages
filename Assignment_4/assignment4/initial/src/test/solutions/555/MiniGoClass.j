.source MiniGoClass.java
.class public MiniGoClass
.super java.lang.Object
.field static final MAX I

.method public static init([I[Z)V
.var 0 is q [I from Label0 to Label1
.var 1 is v [Z from Label0 to Label1
Label0:
Label2:
	getstatic MiniGoClass/MAX I
	newarray int
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	dup
	iconst_2
	iconst_0
	iastore
	dup
	iconst_3
	iconst_0
	iastore
	dup
	iconst_4
	iconst_0
	iastore
	astore_0
	getstatic MiniGoClass/MAX I
	newarray boolean
	dup
	iconst_0
	iconst_0
	bastore
	dup
	iconst_1
	iconst_0
	bastore
	dup
	iconst_2
	iconst_0
	bastore
	dup
	iconst_3
	iconst_0
	bastore
	dup
	iconst_4
	iconst_0
	bastore
	astore_1
Label3:
Label1:
	return
.limit stack 54
.limit locals 2
.end method

.method public static bfs([[II)V
.var 0 is graph [[I from Label0 to Label1
.var 1 is start I from Label0 to Label1
Label0:
Label2:
.var 2 is visited [Z from Label2 to Label3
	getstatic MiniGoClass/MAX I
	newarray boolean
	astore_2
.var 3 is queue [I from Label2 to Label3
	getstatic MiniGoClass/MAX I
	newarray int
	astore_3
	aload_3
	aload_2
	invokestatic MiniGoClass/init([I[Z)V
.var 4 is front I from Label2 to Label3
	iconst_0
	istore 4
.var 5 is rear I from Label2 to Label3
	iconst_0
	istore 5
	aload_2
	iload_1
	iconst_1
	bastore
	aload_3
	iload 5
	iload_1
	iastore
	iload 5
	iconst_1
	iadd
	istore 5
Label4:
	iload 4
	iload 5
	if_icmpge Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
Label8:
.var 6 is u I from Label8 to Label9
	aload_3
	iload 4
	iaload
	istore 6
	iload 4
	iconst_1
	iadd
	istore 4
	iload 6
	invokestatic io/putInt(I)V
	new String_MiniGo
	dup
	ldc " "
	invokespecial String_MiniGo/<init>(Ljava/lang/String;)V
	invokevirtual String_MiniGo/getValue()Ljava/lang/String;
	invokestatic io/putString(Ljava/lang/String;)V
Label12:
.var 7 is v I from Label12 to Label13
	iconst_0
	istore 7
Label14:
	iload 7
	getstatic MiniGoClass/MAX I
	if_icmpge Label16
	iconst_1
	goto Label17
Label16:
	iconst_0
Label17:
	ifle Label11
	goto Label15
Label10:
	iload 7
	iconst_1
	iadd
	istore 7
	goto Label14
Label15:
Label18:
	aload_0
	iload 6
	aaload
	iload 7
	iaload
	iconst_1
	if_icmpne Label20
	iconst_1
	goto Label21
Label20:
	iconst_0
Label21:
	aload_2
	iload 7
	baload
	ifgt Label22
	iconst_1
	goto Label23
Label22:
	iconst_0
Label23:
	iand
	ifle Label24
Label26:
Label27:
	aload_2
	iload 7
	iconst_1
	bastore
	aload_3
	iload 5
	iload 7
	iastore
	iload 5
	iconst_1
	iadd
	istore 5
Label28:
Label24:
Label25:
Label19:
	goto Label10
Label11:
Label13:
Label9:
	goto Label4
Label5:
Label3:
Label1:
	return
.limit stack 22
.limit locals 8
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
Label2:
.var 1 is graph [[I from Label2 to Label3
	getstatic MiniGoClass/MAX I
	getstatic MiniGoClass/MAX I
	multianewarray [[I 2
	dup
	iconst_0
	aaload
	iconst_0
	iconst_0
	iastore
	dup
	iconst_0
	aaload
	iconst_1
	iconst_1
	iastore
	dup
	iconst_0
	aaload
	iconst_2
	iconst_0
	iastore
	dup
	iconst_0
	aaload
	iconst_3
	iconst_0
	iastore
	dup
	iconst_0
	aaload
	iconst_4
	iconst_0
	iastore
	dup
	iconst_1
	aaload
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	aaload
	iconst_1
	iconst_0
	iastore
	dup
	iconst_1
	aaload
	iconst_2
	iconst_1
	iastore
	dup
	iconst_1
	aaload
	iconst_3
	iconst_0
	iastore
	dup
	iconst_1
	aaload
	iconst_4
	iconst_0
	iastore
	dup
	iconst_2
	aaload
	iconst_0
	iconst_0
	iastore
	dup
	iconst_2
	aaload
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	aaload
	iconst_2
	iconst_0
	iastore
	dup
	iconst_2
	aaload
	iconst_3
	iconst_1
	iastore
	dup
	iconst_2
	aaload
	iconst_4
	iconst_0
	iastore
	dup
	iconst_3
	aaload
	iconst_0
	iconst_0
	iastore
	dup
	iconst_3
	aaload
	iconst_1
	iconst_0
	iastore
	dup
	iconst_3
	aaload
	iconst_2
	iconst_1
	iastore
	dup
	iconst_3
	aaload
	iconst_3
	iconst_0
	iastore
	dup
	iconst_3
	aaload
	iconst_4
	iconst_1
	iastore
	dup
	iconst_4
	aaload
	iconst_0
	iconst_0
	iastore
	dup
	iconst_4
	aaload
	iconst_1
	iconst_0
	iastore
	dup
	iconst_4
	aaload
	iconst_2
	iconst_0
	iastore
	dup
	iconst_4
	aaload
	iconst_3
	iconst_1
	iastore
	dup
	iconst_4
	aaload
	iconst_4
	iconst_0
	iastore
	astore_1
	aload_1
	iconst_0
	invokestatic MiniGoClass/bfs([[II)V
Label3:
Label1:
	return
.limit stack 104
.limit locals 2
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
	iconst_5
	putstatic MiniGoClass/MAX I
Label0:
Label1:
	return
.limit stack 2
.limit locals 0
.end method
