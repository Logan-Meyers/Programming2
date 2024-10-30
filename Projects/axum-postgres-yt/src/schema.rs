/*
Validation here, such as types and objects here
*/

use serde::{Deserialize, Serialize};

// when getting all notes, these are the filter options
// page #
// # to limit at, such as '10'
#[derive(Deserialize, Debug, Default)]
pub struct FilterOptions {
    pub page: Option<usize>,
    pub limit: Option<usize>,
}

// When interacting with a particular note, the 'id' will be send
// in the params as a String
#[derive(Deserialize, Debug)]
pub struct ParamOptions {
    pub id: String,
}

// When creating a note, it needs the following:
// - title: String
// - content: String
// - category: Option<String>
// - published: Option<bool>
// where category and published are optionally serialized into the json
// they also don't include created_at or updated_at because that'll be updated by us
#[derive(Serialize, Deserialize, Debug)]
pub struct CreateNoteSchema {
    pub title: String,
    pub content: String,
    pub number: i32,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub category: Option<String>,
    #[serde(skip_serializing_if = "Option::is_none")]
    pub published: Option<bool>,
}

// when updating a note, any of the following attributes may be set
#[derive(Serialize, Deserialize, Debug)]
pub struct UpdateNoteSchema {
    pub title: Option<String>,
    pub content: Option<String>,
    pub category: Option<String>,
    pub published: Option<bool>
}
