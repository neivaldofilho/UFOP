#include<iostream>

class Node {
public:
    int key;
    Node* left;
    Node* right;

    Node(int key) {
        this->key = key;
        left = right = NULL;
    }
};

class BST {
private:
    Node* root;

public:
    BST() {
        root = NULL;
    }

    Node* search(Node* node, int key) {
        if (node == NULL || node->key == key) {
            return node;
        }
        if (node->key < key) {
            return search(node->right, key);
        }
        return search(node->left, key);
    }
    Node* insert(Node* node, int key) {
        if (node == NULL) {
            return new Node(key);
        }
        if (key < node->key) {
            node->left = insert(node->left, key);
        } else if (key > node->key) {
            node->right = insert(node->right, key);
        }
        return node;
    }

    void insert(int key) {
        root = insert(root, key);
    }

    Node* search(int key) {
        return search(root, key);
    }
};
