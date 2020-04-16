# Binet-Tensor-Product
[Jacques Binet](http://mathshistory.st-andrews.ac.uk/Biographies/Binet.html) is thought to have developed the formalizations for the [matrix product](https://en.wikipedia.org/wiki/Matrix_multiplication). In this work I am developing an extension to his idea, and in his recognition I would like to name this extension after him as the *Binet Tensor Product* (BTP).

# Problem
Sometimes we don't have specific names for things because they're small rearrangements of other well-known concepts and don't command enough attention to have a name. I don't know if I'm in that situation, but I've found myself with a concept but not a name. I'd like to be able to learn more about what professionals have studied around this concept, but searchs online have only given me other concepts. 

The concept I'm interested in a generalization I came up with on my own for the product of matrices. Note that I came up with it on my own, but I'm not experienced enough with the related disciplines to even have a qualified opinion on whether I'm the first to think it. My gut feeling is this idea is too obvious to not be either (1) [already defined and worked out][1] by professional mathematicians or (2) was shown not to merit further development. Still, I play with these ideas as a hobby and would like to know more.

# Definition
 The generalization focuses on the mantra that so many students learn when taking their first course in linear algegra: *row-against-column*, which I abbreviate to RAC. I don't have an elegant definition, so please humour showing you what I mean by example.

For vectors,
$$\vec{v}^T \vec{u} = \sum_i^n v_iu_i$$
which is our familiar dot product of vectors. Likewise, my generalization for matrices is the same as canonically taught:
$$AB = [A\vec{b}_1 A\vec{b}_2 ... A\vec{b}_n]$$
which is to say that we can multiple the matrix $A$  against the column vectors of $B$. Where it becomes apparent that I'm focusing on the *row-against-column* concept is when we reach 3-tensors, which I analogize to them being like a matrix that contains vectors. Let's say I have the following two 3-tensors with shape 3x3x3:

$$A = \begin{bmatrix}
\vec{a}_{1,1} & \vec{a}_{1,2} & \vec{a}_{1,3}\\
\vec{a}_{2,1} & \vec{a}_{2,2} & \vec{a}_{2,3}\\
\vec{a}_{3,1} & \vec{a}_{3,2} & \vec{a}_{3,3}
\end{bmatrix} 
= 
\begin{bmatrix}
\begin{bmatrix}a_{1,1,1} \\ a_{1,1,2} \\ a_{1,1,3} \end{bmatrix} & \begin{bmatrix}a_{1,2,1} \\ a_{1,2,2} \\ a_{1,2,3} \end{bmatrix} & \begin{bmatrix}a_{1,3,1} \\ a_{1,3,2} \\ a_{1,3,3}\end{bmatrix}\\
\begin{bmatrix}a_{2,1,1} \\ a_{2,1,2} \\ a_{2,1,3} \end{bmatrix} & \begin{bmatrix}a_{2,2,1} \\ a_{2,2,2} \\ a_{2,2,3} \end{bmatrix} & \begin{bmatrix}a_{2,3,1} \\ a_{2,3,2} \\ a_{2,3,3}\end{bmatrix}\\
\begin{bmatrix}a_{3,1,1} \\ a_{3,1,2} \\ a_{3,1,3} \end{bmatrix} & \begin{bmatrix}a_{3,2,1} \\ a_{3,2,2} \\ a_{3,2,3} \end{bmatrix} & \begin{bmatrix}a_{3,3,1} \\ a_{3,3,2} \\ a_{3,3,3}\end{bmatrix}
\end{bmatrix}$$

$$B = \begin{bmatrix}
\vec{b}_{1,1} & \vec{b}_{1,2} & \vec{b}_{1,3}\\
\vec{b}_{2,1} & \vec{b}_{2,2} & \vec{b}_{2,3}\\
\vec{b}_{3,1} & \vec{b}_{3,2} & \vec{b}_{3,3}
\end{bmatrix} 
= 
\begin{bmatrix}
\begin{bmatrix}b_{1,1,1} \\ b_{1,1,2} \\ b_{1,1,3} \end{bmatrix} & \begin{bmatrix}b_{1,2,1} \\ b_{1,2,2} \\ b_{1,2,3} \end{bmatrix} & \begin{bmatrix}b_{1,3,1} \\ b_{1,3,2} \\ b_{1,3,3}\end{bmatrix}\\
\begin{bmatrix}b_{2,1,1} \\ b_{2,1,2} \\ b_{2,1,3} \end{bmatrix} & \begin{bmatrix}b_{2,2,1} \\ b_{2,2,2} \\ b_{2,2,3} \end{bmatrix} & \begin{bmatrix}b_{2,3,1} \\ b_{2,3,2} \\ b_{2,3,3}\end{bmatrix}\\
\begin{bmatrix}b_{3,1,1} \\ b_{3,1,2} \\ b_{3,1,3} \end{bmatrix} & \begin{bmatrix}b_{3,2,1} \\ b_{3,2,2} \\ b_{3,2,3} \end{bmatrix} & \begin{bmatrix}b_{3,3,1} \\ b_{3,3,2} \\ b_{3,3,3}\end{bmatrix}
\end{bmatrix}$$

then I'd write this special product as

$$A \cdot B = \begin{bmatrix}
\vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1} & \vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1} & \vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1}\\
\vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1} & \vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1} & \vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1}\\
\vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1} & \vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1} & \vec{a}_{1,1} \cdot \vec{b}_{1,1} + \vec{a}_{1,2} \cdot \vec{b}_{2,1} + \vec{a}_{1,3} \cdot \vec{b}_{3,1}
\end{bmatrix} 
$$



  [1]: https://math.stackexchange.com/questions/3493712/what-do-you-call-this-kind-of-matrix-product
