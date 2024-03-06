import React from 'react';
import {View, Text, Image, StyleSheet, TouchableOpacity} from 'react-native';

const imgCheck = require('../assets/check.png');

export default class Checkbox extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            isComplete: props.isChecked,
        };
    }

    toggleCheck() {
        let status = this.state.isComplete;
        this.setState({
            isComplete: !status,
        });

        // Notify any listeners of the state change
        if (this.props.onToggleChange) {
            this.props.onToggleChange(this.props.item, !status);
        }
    }

    render() {
      let {task} = this.props;
        return (
            <View style={styles.container}>
                <TouchableOpacity onPress={() => this.toggleCheck()}>
                    <View style={this.state.isComplete ? styles.boxChecked : styles.box}>
                        {this.state.isComplete && (
                            <Image source={imgCheck} style={styles.check} />
                        )}
                    </View>
                </TouchableOpacity>
                <Text
                    style={this.state.isComplete ? styles.titleComplete : styles.title}>
                    {task.title}
                </Text>
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flexDirection: 'row',
        alignItems: 'center',
        padding: 5,
    },
    box: {
        borderColor: '#2699FB',
        borderWidth: 2,
        borderStyle: 'solid',
        padding: 3,
        width: 30,
        height: 30,
        justifyContent: 'center',
        alignItems: 'center',
    },
    boxChecked: {
        borderColor: '#2699FB',
        borderWidth: 2,
        borderStyle: 'solid',
        padding: 3,
        width: 30,
        height: 30,
        justifyContent: 'center',
        alignItems: 'center',
        backgroundColor: '#2699FB',
    },
    check: {
        width: 24,
        height: 24,
    },
    title: {
        color: '#2699FB',
        fontWeight: 'bold',
        marginLeft: 15,
        fontSize: 18,
    },
    titleComplete: {
        color: 'gray',
        marginLeft: 15,
        fontSize: 18,
    },
});

