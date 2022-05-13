//import {makeAutoObservable} from "mobx";
//
//export default class FinanceStore {
//    constructor() {
//        this._operations = {
//            {id: 1, date: "2022-05-07", kind: "income", amount: 8430.00, description: "транзакция 1"},
//            {id: 2, date: "2021-01-24", kind: "outcome", amount: 1430.00, description: "транзакция 2"},
//            {id: 3, date: "2020-11-17", kind: "income", amount: 12430.00, description: "транзакция 3"},
//            {id: 4, date: "2018-04-15", kind: "outcome", amount: 8430.00, description: "транзакция 4"},
//        }
//        this._types = {}
//        makeAutoObservable(this)
//    }
//
//    setTypes(types) {
//        this._types = types
//    }
//    setOperations(operations) {
//        this._operations = operations
//    }
//
//    get types() {
//        return this._types
//    }
//    get operations() {
//        return this._operations
//    }
//}