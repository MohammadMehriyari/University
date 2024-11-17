/*Function for sum of nodes*/
int sumofnodes(struct node *root)
{
    int rightsubtree, leftsubtree, sum = 0;
    if(root != NULL)
    {
        leftsubtree = sumofnodes(root->left);
        rightsubtree = sumofnodes(root->right);
        sum = (root->info) + leftsubtree + rightsubtree;
        return sum;
    }
}