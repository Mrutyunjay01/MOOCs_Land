import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.blueGrey[900],
        appBar: AppBar(
          title: Text("Kaggle"),
          backgroundColor: Colors.blueAccent[900],
        ),
        body: Center(
          child: Image(
            image: NetworkImage(
                'https://storage.googleapis.com/kaggle-media/Kaggle%20Brand%20Guidelines%20CMS/png%20logo.png'),
          ),
        ),
      ),
    ),
  );
}
