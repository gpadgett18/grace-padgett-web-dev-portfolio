import React from 'react';
import { SafeAreaView, StyleSheet, View, Text, TextInput } from 'react-native';
import Header from '../components/Header';
import BlueButton from '../components/BlueButton';
import Checkbox from '../components/Checkbox';

let tasks = [
    {
        title: 'My first completed task',
        checked: true,
    },
    {
        title: 'My second task',
        checked: false,
    },
    {
        title: 'My third task',
        checked: false,
    },
];

export default class MainScreen extends React.Component {
  
  state = {
    inputValue: '',
  }

  handleTextChange = (val) => {
    this.setState({ inputValue: val });
  }

  createTask = () => {
    if (this.state.inputValue) {
      console.log("Create task: " + this.state.inputValue);
    } else {
      alert('Enter a task')
    }
  }

  handleToggleChanged = (title, checked) => {
    console.log("Check = " + checked);
  }

  renderTasks() {
    let props = []
    for(let i = 0; i < tasks.length; i++) {
      let s = tasks[i];
      props.push( <Checkbox task={s} /> );
    }
    
    return props;
  }

  render() {
    let { inputValue } = this.state;

    return (
      <SafeAreaView style={styles.container}>
        <Header instructions="Organize your tasks" />
        <View style={styles.addContainer}>
          <Text style={styles.inputLabel}>Add Text</Text>
          <View style={styles.addForm}>
            <TextInput 
              style={styles.addInput}
              onChangeText={this.handleTextChange} 
            />
            <BlueButton 
              title="Add" 
              onPress={this.createTask}
            />
          </View>
        </View>
        <View style={{margin: 20}}>
          < Checkbox task ={this.renderTasks} />
        </View>
      </SafeAreaView>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    backgroundColor: '#ffffff',
    flex: 1,
  },
  addContainer: {
    margin: 20,
  },
  addForm: {
    flexDirection: 'row',
  },
  inputLabel: {
    color: '#2699FB',
    fontSize: 12,
    marginBottom: 5,
  },
  addInput: {
    borderWidth: 2,
    borderColor: '#2699FB',
    borderStyle: 'solid',
    padding: 8,
    flex: 1,
    marginRight: 10,
  },
});
