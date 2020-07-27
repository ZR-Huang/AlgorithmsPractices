#include <iostream>
#define LH 1        // 左高
#define EH 0        // 等高
#define RH -1       // 右高
using namespace std;


typedef struct Node {
    int data;
    int bf;     // 平衡因子
    Node *lchild;
    Node *rchild;
    Node(int x) : data(x), bf(0), lchild(NULL), rchild(NULL) {}
} BSTNode, *BSTNode_p;

class AVLTree {
private:
    void rightRotate(BSTNode_p &p){
        // 对以 *p 为根的二叉排序树作右旋处理，处理之后p指向新的树根结点，即旋转
        // 处理之前的左子树的根结点
        BSTNode_p lc = p->lchild;   // lc指向的 *p 的左子树根结点
        p->lchild = lc->rchild;   // lc的右子树挂接为 *p 的左子树
        lc->rchild = p;
        p = lc;
    }

    void leftRotate(BSTNode_p &p) {
        // 对以*p为根的二叉排序树做左旋处理，处理之后p指向新的树根结点，即旋转
        // 处理之前的右子树的根结点
        BSTNode_p rc = p->rchild; // rc 指向的*p的右子树根结点
        p->rchild = rc->lchild;     // rc的左子树挂接为*p的右子树
        rc->lchild = p;
        p = rc;
    }

    void leftBalance (BSTNode_p &T) {
        // 对以指针T所指结点为根的二叉树作左平衡旋转处理，本算法结束时，指针T指向
        // 新的根结点
        BSTNode_p lc = T->lchild;       // lc指向*T的左子树根结点
        switch (lc->bf)     // 检查*T的左子树的平衡度，并作相应平衡处理
        {
            case LH:            // 新结点插入在*T的左孩子的左子树上，要做单右旋处理
                T->bf = lc->bf = EH;
                rightRotate(T);
                break;
            case RH:            // 新结点插入在*T的左孩子的右子树上，要作双旋处理
                BSTNode_p rd = lc->rchild;    // rd指向*T的左孩子的右子树根
                switch (rd->bf) // 修改*T及其左孩子的平衡因子   
                {
                    case LH: T->bf = RH; lc->bf = EH; break;
                    case EH: T->bf = lc->bf = EH; break;
                    case RH: T->bf = EH; lc->bf = LH; break;
                }
                rd->bf = EH;
                leftRotate(T->lchild);
                rightRotate(T);
        }
    }

public:
    int Insert(BSTNode_p &T, int e, bool &taller) {
        // 若在平衡的二叉排序树T中不存在和e有相同关键字的结点，则插入一个数据元素
        // 为e的新结点，并返回1，否则返回0.若因插入而使二叉排序树失去平衡，则作平衡
        // 旋转处理，布尔变量taller反映长高与否
        if (!T) {
            // 插入新结点，树“长高”，置taller为TRUE
            BSTNode_p T = (BSTNode_p) malloc (sizeof(BSTNode));
            T->data = e;
            T->bf = EH;
            taller = true;
        } else {
            if (T->data == e){
                taller = false;
                return 0;
            }
            if (e < T->data) {
                if(!Insert(T->lchild, e, taller)) return 0;
                if (taller)
                    switch (T->bf) {
                        case LH:
                            leftBalance(T); taller = false; break;
                        case EH:
                            T->bf = LH; taller = true; break;
                        case RH:
                            T->bf = EH; taller = false; break;
                    }
            } else {
                if (!Insert(T->rchild, e, taller)) return 0;
                if(taller)
                    switch(T->bf) {
                        case LH:
                            T->bf = EH; taller = false; break;
                        case EH:
                            T->bf = RH; taller = true; break;
                        case RH:
                            rightBalance(T); taller = false; break;
                    }
            }
        }
        return 1;
    }

};
