import 'package:flutter/material.dart';

void main() {
  runApp(
    MaterialApp(
        home: Scaffold(
          backgroundColor: Colors.blueGrey,  //changes the whole bg of the App
          appBar: AppBar(
            title: Text('My first App'),  // title of the Application
            backgroundColor: Colors.blueGrey[900],  // Colors class provides a bunch of colors

          ),
          body: Center(
            child: Image(
              // image: NetworkImage('https://flutter.github.io/assets-for-api-docs/assets/widgets/owl.jpg'),
              // Upper chunk of code is used to add image via url
              // to add image from existing folder
              image: AssetImage('images/ML4e-Logo.png'),
            ),
          )
        ),
      ),
    );
}